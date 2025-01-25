from dataframes import get_countries_gdp
'''
pip install openpyxl
    Установить библиотеку openpyxl
'''
df = get_countries_gdp()
try:
    # Запись DataFrame в файл Excel
    df.to_excel('countries_gdp.xlsx', sheet_name='GDP Data', engine='openpyxl')
    print("Данные успешно записаны в файл 'countries_gdp.xlsx'.")
except Exception as e:
    print(f"Произошла ошибка при записи в Excel: {e}")