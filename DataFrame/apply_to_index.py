import pandas as pd
from dataframes import get_countries_gdp
'''
применить к индексу
'''
# Предположим, что функция get_countries_gdp() возвращает DataFrame
df = get_countries_gdp()
print('df до изминения')
print(df)
def f(x: pd.Series) -> pd.Series:
    if x.name == 'population' or x.name == 'region':
        return x
    else:
        return x / 1000

df = df.rename(columns={
    'gdp': 'gdp_trln'
})
print('df после изменения')
print(df.apply(f, axis='index'))