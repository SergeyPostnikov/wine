import pandas


def get_records():
    goods = {}
    excel_data_df = pandas.read_excel(
        'wine.xlsx', 
        sheet_name='Лист1',
        na_values=None, 
        keep_default_na=False)

    for product in excel_data_df.to_dict(orient='records'):
        if product['Категория'] in goods:
            goods[product['Категория']].append(product)
        else:
            goods[product['Категория']] = [product]
    return goods


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_records())
