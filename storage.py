import pandas


def get_records():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1')
    return excel_data_df.to_dict(orient='records')
