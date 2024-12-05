from icrawler.builtin import GoogleImageCrawler


folder_path = "watch_images"

google_Crawler = GoogleImageCrawler(
    storage={
        "root_dir": "watch_images"
    }
)

import pandas as pd

watch_data = pd.read_csv("test.csv", index_col=None)

import time
import os

for i in range(len(watch_data)):
    google_Crawler.crawl(keyword=watch_data["name"][i], max_num=1)
    # Đổi tên file 0001.png thành INDEX của đồng hồ

    # Thư mục chứa các file

    # Lấy danh sách các file trong thư mục
    files = os.listdir(folder_path)

    # Đổi tên các file
    for file in files:
        if file.startswith("000001."):
            new_name = file.replace("000001.", f"{i}.")
            os.rename(
                os.path.join(folder_path, file), os.path.join(folder_path, new_name)
            )