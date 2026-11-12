# Experiment Report: CLIP-based Image Clustering

## 1. Objective

This experiment explores whether CLIP image representations
can support the organization of photographic collections
through unsupervised clustering.

## 2. Dataset

A sample of 500 images was selected from the AVA dataset.
The image IDs were checked against the corresponding image files.

## 3. Feature Representation

Each image is represented by a 512-dimensional CLIP embedding.
The embeddings are L2-normalized before clustering.

The current experiment uses CLIP embeddings only.
Aesthetic scores and the 12 structural features are not used
as clustering inputs.

## 4. Clustering Method

K-means is applied with random_state = 42 and n_init = 20.
The number of clusters is tested from K = 2 to K = 12.

## 5. Evaluation

The following measures are recorded:

- Inertia
- Silhouette Score
- Davies-Bouldin Index
- Minimum and maximum cluster sizes

Visual inspection of cluster contact sheets is also used
to examine within-cluster similarities and differences.

## 6. Preliminary Observations

Visual inspection suggests recurring groups involving
portraits and people, animals, natural landscapes,
urban environments, objects and abstract compositions.

However, clusters are not fully homogeneous.
Some images may share several characteristics, including
subject matter, composition and color.

For K = 4, 6 and 7, the observed metrics are:

| Metric | K = 4 | K = 6 | K = 7 |
|---|---:|---:|---:|
| Silhouette Score | 0.0401 | 0.0413 | 0.0424 |
| Davies-Bouldin Index | 3.925 | 3.681 | 3.736 |
| Minimum cluster size | 60 | 61 | 36 |
| Maximum cluster size | 159 | 134 | 140 |

K = 7 has the highest Silhouette Score among these three
configurations, while K = 6 has the lowest Davies-Bouldin
Index and a relatively balanced cluster size distribution.

K = 6 is therefore retained as a candidate for further
qualitative inspection. It is not claimed to be the
objectively optimal number of clusters.

## 7. Limitations

The sample contains 500 images and may not represent
the full dataset.

The relatively low Silhouette Scores indicate that
the clusters are not strongly separated.

CLIP embeddings encode multiple kinds of visual information.
The observed clusters should not be interpreted as strict
or mutually exclusive semantic categories.

## 8. Next Steps

1. Conduct color-based clustering using HSV features.
2. Compare the effects of different feature representations.
3. Validate CLIP-based clustering on the full dataset.
4. Further investigate cluster interpretability and limitations.
