import pandas
from collections import defaultdict


def get_records():
    records = defaultdict(list)
    excel_data_df = pandas.read_excel(
        'wine.xlsx', 
        sheet_name='Лист1',
        na_values=None, 
        keep_default_na=False)
    for product in excel_data_df.to_dict(orient='records'):
        records[product['Категория']].append(product)
    return records


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_records())
