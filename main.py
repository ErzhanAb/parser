# Import modules
import os
from utils.get_links import get_links
from utils.get_dataset import get_dataset
from utils.read_dataset import read_dataset


# Creating 'outputs' directory
if not os.path.exists('outputs'):
    os.mkdir('outputs')


# Creating a 'links.json' file
links = get_links(int(input('How many pages to parse? ')))


# Creating a 'dataset.jsonl' file
get_dataset(links)


# Reading file 'dataset.jsonl'
dataset = read_dataset('outputs/dataset.jsonl')