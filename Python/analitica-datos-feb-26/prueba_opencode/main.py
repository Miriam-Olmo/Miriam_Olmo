import pandas as pd
import json


def load_books(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    print(df)


if __name__ == '__main__':
    load_books('data/libros.json')