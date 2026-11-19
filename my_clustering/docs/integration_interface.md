# Integration Interface

## Purpose

This document describes how the Visual Clustering module
can connect with the group's aesthetic prediction
and recommendation module.

## Current Output

The clustering module produces a cluster assignment
for each image.

Recommended output fields:

| Field | Description |
|---|---|
| image_id | Unique image identifier |
| cluster_id | K-means cluster assignment |
| feature_type | Feature representation used, e.g. CLIP |
| k | Number of clusters used |

## Example

| image_id | cluster_id | feature_type | k |
|---|---:|---|---:|
| 191162 | 2 | CLIP | 6 |
| 906149 | 0 | CLIP | 6 |

These values are illustrative examples of the output format.

## Integration

The cluster assignment can be joined with aesthetic
prediction results using `image_id`.

This enables the group to explore image discovery
using both visual similarity and predicted aesthetic quality.

## Important Notes

Cluster IDs are arbitrary identifiers.
They do not represent aesthetic rankings or quality levels.

The current cluster assignments are preliminary and
should not be treated as final image categories.
