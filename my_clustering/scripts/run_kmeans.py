
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

DATA_PATH = Path("data/sample_500.parquet")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(exist_ok=True)

print("正在读取数据...")
df = pd.read_parquet(DATA_PATH)

X = np.stack(df["clip_embedding"].values).astype(np.float32)
image_ids = df["image_id"].values

print("图片数量:", len(X))
print("Embedding维度:", X.shape[1])

if not np.isfinite(X).all():
    raise ValueError("Embedding中存在NaN或Inf")

norms = np.linalg.norm(X, axis=1)
if np.any(norms == 0):
    raise ValueError("发现零向量")

X = X / norms[:, None]
print("归一化完成，开始K-means实验")

results = []

for k in range(2, 13):
    print(f"\n正在运行 K={k}...")

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )

    labels = model.fit_predict(X)

    results.append({
        "K": k,
        "Inertia": model.inertia_,
        "Silhouette": silhouette_score(X, labels),
        "Davies_Bouldin": davies_bouldin_score(X, labels),
        "Min_Cluster_Size": np.bincount(labels).min(),
        "Max_Cluster_Size": np.bincount(labels).max()
    })

    pd.DataFrame({
        "image_id": image_ids,
        "cluster": labels
    }).to_csv(RESULT_DIR / f"labels_k{k}.csv", index=False)

metrics_df = pd.DataFrame(results)
metrics_df.to_csv(RESULT_DIR / "kmeans_metrics.csv", index=False)

print("\n========== 实验完成 ==========")
print(metrics_df.round(4).to_string(index=False))
print("\n结果已保存到 results/ 文件夹")

