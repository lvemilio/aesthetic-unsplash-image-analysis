from pathlib import Path
import pandas as pd
from PIL import Image, ImageDraw
import math

BASE = Path(__file__).resolve().parent
IMAGE_DIR = BASE / "images"
RESULT_DIR = BASE / "results"
OUTPUT_DIR = RESULT_DIR / "contact_sheets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 先观察这三个 K 值
K_VALUES = [4, 6, 7]

# 每个群组最多展示多少张图片
MAX_IMAGES = 30

for k in K_VALUES:
    label_file = RESULT_DIR / f"labels_k{k}.csv"
    df = pd.read_csv(label_file)

    print(f"\n正在处理 K={k}")

    for cluster_id, group in df.groupby("cluster"):
        group = group.head(MAX_IMAGES)

        thumbnails = []

        for _, row in group.iterrows():
            image_id = str(row["image_id"])
            image_path = IMAGE_DIR / f"{image_id}.jpg"

            if not image_path.exists():
                continue

            try:
                img = Image.open(image_path).convert("RGB")
                img.thumbnail((150, 120))
                thumbnails.append((image_id, img.copy()))
            except Exception as e:
                print(f"跳过图片 {image_id}: {e}")

        if not thumbnails:
            print(f"Cluster {cluster_id}: 没有找到本地图片")
            continue

        cols = 5
        cell_w, cell_h = 170, 155
        rows = math.ceil(len(thumbnails) / cols)

        sheet = Image.new(
            "RGB",
            (cols * cell_w, rows * cell_h),
            "white"
        )
        draw = ImageDraw.Draw(sheet)

        for i, (image_id, img) in enumerate(thumbnails):
            x = (i % cols) * cell_w
            y = (i // cols) * cell_h

            px = x + (cell_w - img.width) // 2
            py = y

            sheet.paste(img, (px, py))
            draw.text(
                (x + 5, y + 125),
                image_id,
                fill="black"
            )

        output_file = OUTPUT_DIR / f"k{k}_cluster{cluster_id}.jpg"
        sheet.save(output_file, quality=90)

        print(
            f"Cluster {cluster_id}: "
            f"{len(thumbnails)} 张预览图片 -> {output_file}"
        )

print("\n完成！图片预览保存在 results/contact_sheets/")
