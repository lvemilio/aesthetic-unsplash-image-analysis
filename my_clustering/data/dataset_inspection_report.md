# AVA 500-Record Sample Inspection

## Dataset structure

- Source file: `/Users/mjn/Desktop/mjn编程学习/周二课程图片分析/aesthetic-unsplash-image-analysis/data/ava_cleaned_features.parquet`
- Source row count: 20420
- Columns: `image_id`, `mean_score`, `std_score`, `total_votes`, `rating_counts`, `structural_features`, `clip_embedding`
- Original Parquet image ID column: `image_id`
- Original image ID dtype: `str`
- Original image ID format: decimal digit strings with no filename extension; observed lengths: 3, 4, 5, 6
- CLIP embedding column: `clip_embedding` (512 values per valid record)
- Structural feature column: `structural_features` (12 values per valid record)

The 12 structural-feature values are ordered as:
`brightness, contrast, center_ratio, r_mean, g_mean, b_mean, r_std, g_std, b_std, aspect_ratio, width, height`.

## Data quality

- Missing image IDs: 0
- Duplicate image IDs: 0
- Records with invalid CLIP embeddings: 0
- Records with invalid structural feature vectors: 0
- Records valid for sampling: 20420

### Missing values by column

| Column | Missing values |
|---|---:|
| `image_id` | 0 |
| `mean_score` | 0 |
| `std_score` | 0 |
| `total_votes` | 0 |
| `rating_counts` | 0 |
| `structural_features` | 0 |
| `clip_embedding` | 0 |

## Reproducible sample

- Selected records: 500
- Random seed: 42
- Example selected IDs: `253900`, `191162`, `906149`, `417619`, `168297`

`sample_500.parquet` retains every source column and preserves each original
`image_id` value without formatting changes. `sample_500_image_ids.csv`
contains only the corresponding 500 original `image_id` values.

`mean_score` is retained as source metadata only; it is not a clustering
feature.
