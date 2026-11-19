# Model and Algorithm Selection

## 1. CLIP: Feature Extraction

CLIP embeddings are used as the initial image representation.

Reasons for selection:

- They provide high-dimensional image representations.
- They capture semantic and visual information.
- Precomputed embeddings are already available in the dataset.
- They provide a useful baseline for image clustering.

Important clarification:

CLIP is a pretrained feature extraction model in this experiment.
The CLIP model itself is not trained or fine-tuned here.

The exact CLIP model variant and embedding provenance
should be confirmed from the dataset documentation.

## 2. K-means: Clustering Algorithm

K-means is selected as the baseline clustering algorithm.

Reasons for selection:

- It is relatively straightforward to implement and interpret.
- It allows systematic comparison across different K values.
- It provides cluster assignments and centroids.
- Its results can be evaluated using internal clustering metrics.

## 3. Preprocessing and Parameters

- Input: 512-dimensional CLIP embeddings
- Normalization: L2 normalization
- Algorithm: K-means
- Random state: 42
- n_init: 20
- K range: 2 to 12

## 4. Evaluation Metrics

- Inertia: within-cluster sum of squared distances.
- Silhouette Score: assesses cohesion and separation.
- Davies-Bouldin Index: assesses within-cluster dispersion
  relative to between-cluster separation.
- Cluster size distribution: identifies very small or
  disproportionately large clusters.

No single metric is sufficient to determine the best K.
Quantitative metrics and qualitative inspection are considered together.

## 5. Alternative Feature Representation

HSV color histograms are planned as a second feature
representation. The purpose is to investigate how clustering
changes when color distribution, rather than CLIP embeddings,
is used as the input.
