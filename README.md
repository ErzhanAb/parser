# README

## Description
This project is a web scraper that collects information about car sales from a website. The script parses advertisement links, extracts data, and saves them into `links.json` and `dataset.jsonl` files.

## Project Structure
```
<project_name>/
│── main.py
│── requirements.txt
│── outputs/
│   │── links.json
│   │── dataset.jsonl
│── utils/
│   │── get_links.py
│   │── get_info.py
│   │── get_dataset.py
│   │── read_dataset.py
```

## Installation and Execution
### 1. Clone the Repository
```bash
git clone https://github.com/ErzhanAb/parser.git
cd parser
mkdir outputs
```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Script
```bash
python main.py
```
Then, enter the number of pages you want to parse.

## File Descriptions
- **`main.py`** – The main file that calls all necessary functions.
- **`utils/get_links.py`** – Collects links to advertisements.
- **`utils/get_info.py`** – Extracts information about each car.
- **`utils/get_dataset.py`** – Creates a dataset from the collected data.
- **`utils/read_dataset.py`** – Loads and reads the dataset.
- **`outputs/links.json`** – Contains links to advertisements.
- **`outputs/dataset.jsonl`** – Contains collected car data in JSONL format.

## Additional Notes
- Ensure that you have Python 3.8 or later installed.
- If needed, create the `outputs/` directory manually.

---

Developed for data collection and analysis. Use the script in compliance with applicable laws and terms of use.