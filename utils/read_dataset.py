# Import modules
import json


def read_dataset(file: json) -> list:
    with open(file, 'r', encoding='utf-8') as f:
        dataset = []
        for row in f:
            dataset.append(json.loads(row))
        print()
        print(f'====================================================================================================')
        print(f'''File '{file}' successfully read''')
        print(f'====================================================================================================')
        print()
        return dataset