#!/usr/bin/env python3
"""Create a validated, reproducible 500-record AVA feature sample."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 42
SAMPLE_SIZE = 500
STRUCTURAL_FEATURE_NAMES = [
    "brightness",
    "contrast",
    "center_ratio",
    "r_mean",
    "g_mean",
    "b_mean",
    "r_std",
    "g_std",
    "b_std",
    "aspect_ratio",
    "width",
    "height",
]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PARQUET = PROJECT_ROOT / "data" / "ava_cleaned_features.parquet"
OUTPUT_DIRECTORY = Path(__file__).resolve().parent / "data"


def has_expected_finite_vector(value: object, expected_length: int) -> bool:
    """Return whether a value is a finite numeric vector of the expected length."""
    try:
        vector = np.asarray(value, dtype=np.float32)
    except (TypeError, ValueError):
        return False
    return vector.ndim == 1 and len(vector) == expected_length and np.isfinite(vector).all()


def describe_image_id_format(image_ids: pd.Series) -> str:
    """Describe the source ID representation without converting its values."""
    non_missing_ids = image_ids.dropna()
    are_digit_strings = non_missing_ids.map(
        lambda value: isinstance(value, str) and value.isdecimal()
    ).all()
    lengths = sorted({len(value) for value in non_missing_ids if isinstance(value, str)})
    if are_digit_strings:
        return (
            f"decimal digit strings with no filename extension; observed lengths: "
            f"{', '.join(map(str, lengths))}"
        )
    return "the original Parquet string values; see `sample_500_image_ids.csv`"


def write_inspection_report(
    source: pd.DataFrame,
    valid: pd.DataFrame,
    invalid_embedding_count: int,
    invalid_structural_count: int,
    duplicate_id_count: int,
    sample: pd.DataFrame,
) -> None:
    """Document source structure, ID format, validation, and sampling."""
    report_path = OUTPUT_DIRECTORY / "dataset_inspection_report.md"
    missing_counts = source.isna().sum()
    missing_lines = "\n".join(
        f"| `{column}` | {int(count)} |"
        for column, count in missing_counts.items()
    )
    examples = ", ".join(f"`{image_id}`" for image_id in sample["image_id"].head(5))
    report_path.write_text(
        f"""# AVA 500-Record Sample Inspection

## Dataset structure

- Source file: `{SOURCE_PARQUET}`
- Source row count: {len(source)}
- Columns: {", ".join(f"`{column}`" for column in source.columns)}
- Original Parquet image ID column: `image_id`
- Original image ID dtype: `{source["image_id"].dtype}`
- Original image ID format: {describe_image_id_format(source["image_id"])}
- CLIP embedding column: `clip_embedding` (512 values per valid record)
- Structural feature column: `structural_features` (12 values per valid record)

The 12 structural-feature values are ordered as:
`{", ".join(STRUCTURAL_FEATURE_NAMES)}`.

## Data quality

- Missing image IDs: {int(source["image_id"].isna().sum())}
- Duplicate image IDs: {duplicate_id_count}
- Records with invalid CLIP embeddings: {invalid_embedding_count}
- Records with invalid structural feature vectors: {invalid_structural_count}
- Records valid for sampling: {len(valid)}

### Missing values by column

| Column | Missing values |
|---|---:|
{missing_lines}

## Reproducible sample

- Selected records: {len(sample)}
- Random seed: {RANDOM_SEED}
- Example selected IDs: {examples}

`sample_500.parquet` retains every source column and preserves each original
`image_id` value without formatting changes. `sample_500_image_ids.csv`
contains only the corresponding 500 original `image_id` values.

`mean_score` is retained as source metadata only; it is not a clustering
feature.
""",
        encoding="utf-8",
    )


def main() -> None:
    """Validate the source dataset and write the deterministic sample."""
    if not SOURCE_PARQUET.is_file():
        raise FileNotFoundError(f"Source Parquet file does not exist: {SOURCE_PARQUET}")

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    source = pd.read_parquet(SOURCE_PARQUET)
    required_columns = {"image_id", "clip_embedding", "structural_features"}
    missing_columns = required_columns.difference(source.columns)
    if missing_columns:
        raise ValueError(f"Source dataset is missing required columns: {sorted(missing_columns)}")

    image_ids = source["image_id"]
    duplicate_id_count = int(image_ids.duplicated(keep=False).sum())
    embedding_is_valid = source["clip_embedding"].map(
        lambda value: has_expected_finite_vector(value, 512)
    )
    structural_is_valid = source["structural_features"].map(
        lambda value: has_expected_finite_vector(value, len(STRUCTURAL_FEATURE_NAMES))
    )
    valid_mask = (
        image_ids.notna()
        & ~image_ids.duplicated(keep=False)
        & embedding_is_valid
        & structural_is_valid
    )
    valid = source.loc[valid_mask].copy()
    if len(valid) < SAMPLE_SIZE:
        raise ValueError(
            f"Only {len(valid)} valid records are available; {SAMPLE_SIZE} are required."
        )

    sample = valid.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED).reset_index(drop=True)
    sample.to_parquet(OUTPUT_DIRECTORY / "sample_500.parquet", index=False)
    sample[["image_id"]].to_csv(
        OUTPUT_DIRECTORY / "sample_500_image_ids.csv", index=False
    )
    write_inspection_report(
        source=source,
        valid=valid,
        invalid_embedding_count=int((~embedding_is_valid).sum()),
        invalid_structural_count=int((~structural_is_valid).sum()),
        duplicate_id_count=duplicate_id_count,
        sample=sample,
    )

    print(f"Source rows: {len(source)}")
    print(f"Valid rows: {len(valid)}")
    print(f"Sample rows: {len(sample)}")
    print(f"Output directory: {OUTPUT_DIRECTORY}")


if __name__ == "__main__":
    main()
