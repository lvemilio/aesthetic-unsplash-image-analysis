# Data Documentation

## Dataset

The experiment uses image records from the AVA dataset
used by the group project.

The source dataset contains precomputed CLIP embeddings
and additional structural and aesthetic-related fields.

## Current Sample

- Sample size: 500 images
- Random seed: 42
- CLIP embedding dimension: 512
- Image IDs: stored in the sample ID CSV file
- Image files: retained locally for visual inspection

## Features Used

For the current CLIP clustering experiment:

- `clip_embedding`: used as clustering input

The following fields are not used as clustering inputs:

- Aesthetic mean score
- The 12 structural features

## Preprocessing

The 512-dimensional embeddings are converted into a
feature matrix and L2-normalized before K-means.

## Data Matching

The sample image IDs, Parquet records and local image files
were checked for one-to-one correspondence.

## Data and Licensing Notes

The original dataset and image files remain subject to
their source terms and licensing conditions.

Check the dataset license and group repository policy
before redistributing image files.
