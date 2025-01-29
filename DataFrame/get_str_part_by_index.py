from pandas import DataFrame

"""
Столбец разделения строки и получить последнюю часть строки: 28 августа 1828 -> 1828
"""

df = DataFrame(data=[
    ['А.С. Пушкин', '26 мая 1799'],
    ['М. Ю. Лермонтов', '3 октября 1814'],
    ['Л. Н. Толстой', '28 августа 1828'],
], columns=['writer', 'birth_date'])

df['birth_year'] = df['birth_date'].str.split().str[-1]
print(df)
