# Import modules
import requests
import json
import os
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
from utils.get_info import get_all_info


def get_dataset(links: list) -> None:
    os.environ['TZ'] = 'Asia/Bishkek'
    time.tzset()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('outputs/dataset.jsonl', 'a', encoding='utf-8') as f:
        for url in tqdm(links):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            row = get_all_info(soup)
            row['link'] = url
            row['time'] = current_time
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
        print()
        print()
        print(f'====================================================================================================')
        print(f"""File 'dataset.jsonl' is created in directory 'outputs/dataset.jsonl'""")
        print(f'====================================================================================================')
        print()
        print()