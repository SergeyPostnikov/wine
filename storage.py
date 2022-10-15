import pandas
from collections import defaultdict


def get_products(filepath: str) -> defaultdict:
    products = defaultdict(list)
    excel_data_df = pandas.read_excel(
        io=filepath, 
        sheet_name='Лист1',
        na_values=None, 
        keep_default_na=False)
    for product in excel_data_df.to_dict(orient='records'):
        products[product['Категория']].append(product)
    return products


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_products('wine.xlsx'))
