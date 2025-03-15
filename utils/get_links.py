# Import modules
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_links(pages: int = 1) -> list:
    # Request for site 'mashina.kg'
    URL = 'https://m.mashina.kg/search/all/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Getting URL of n number of pages
    sub_urls = []
    for page in tqdm(range(1, pages + 1)):
        page_url = f'{URL}?page={page}'
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for block_image in soup.find_all('div', class_='list-item list-label'):
            sub_urls.append(f"https://m.mashina.kg{block_image.find('a')['href']}")
    
    # Creating 'links.json'
    with open('outputs/links.json', 'w') as f:
        json.dump(sub_urls, f, indent = 4)
        print()
        print()
        print(f'====================================================================================================')
        print(f"""File 'links.json' is created in directory 'outputs/links.json'""")
        print(f'====================================================================================================')
        print()
        print()

    return sub_urls
