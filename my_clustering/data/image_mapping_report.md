# Sample Image Mapping Report

## Matching method

Selected `image_id` values were converted to strings and compared with the
stems of actual filenames in `/Users/mjn/Desktop/mjn编程学习/周二课程图片分析/ava_500/images`. This verifies the naming
convention instead of assuming an ID is a filename.

## Results

- Selected records: 500
- Local image files inspected: 500
- Exactly matched IDs: 2
- IDs not found locally: 498
- Ambiguous filename stems: 0
- Duplicate filename stems in the local folder: 0
- Local filename IDs found anywhere in the source Parquet: 38
- Local filename IDs absent from the source Parquet: 462

The local files use names such as `123456.jpg`; the comparison used the
filename stem (`123456`) so it works independently of the extension.
Therefore, the 498 unmatched sample IDs are not caused by a filename-format
difference: the local 500-image folder and the source Parquet contain
substantially different ID subsets.

The complete per-record result is in `sample_500_image_ids.csv`.
