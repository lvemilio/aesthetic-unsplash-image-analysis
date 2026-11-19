# Visual Image Clustering

## Project Overview

This module investigates how machine learning can organize
photographic collections based on visual characteristics.

The current preliminary experiment uses CLIP image embeddings
and K-means clustering on a sample of 500 images from the AVA dataset.

## Research Focus

How can different visual feature representations support
the organization and discovery of photographic images
through unsupervised clustering?

## Current Experiments

| Experiment | Feature Representation | Algorithm | Status |
|---|---|---|---|
| Experiment 1 | CLIP embeddings (512 dimensions) | K-means | Preliminary completed |
| Experiment 2 | HSV color histograms | K-means | Planned / in progress |
| Experiment 3 | Style-oriented features | To be determined | Optional |

## Experiment 1: CLIP-based Clustering

- Dataset: 500 sampled images
- Feature: 512-dimensional CLIP embeddings
- Preprocessing: L2 normalization
- Algorithm: K-means
- Random state: 42
- Number of clusters tested: K = 2 to 12
- Evaluation: Inertia, Silhouette Score, Davies-Bouldin Index
  and cluster size distribution

K = 4, 6 and 7 are included for visual comparison.
K = 6 is currently a candidate configuration, not a final
or objectively optimal choice.

## Repository Structure

- `docs/`: experiment documentation and methodology
- `scripts/`: reproducible Python scripts
- `notebooks/`: exploratory analysis notebooks
- `results/`: metrics, cluster labels and visualizations

## Current Status and Limitations

The current results are preliminary and based on 500 images.
The Silhouette Scores are relatively low, suggesting limited
cluster separation in the current feature space.

Color-based clustering and validation on the full dataset
are planned as subsequent experiments.

## Reproducibility

The scripts require the relevant Python dependencies,
the input feature dataset and the corresponding image files
for visual previews.

See the documentation in `docs/` for further details.
