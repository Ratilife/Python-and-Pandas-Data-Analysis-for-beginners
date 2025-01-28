import pandas as pd
from dataframes import get_countries_gdp

# Предположим, что функция get_countries_gdp() возвращает DataFrame
df = get_countries_gdp()

def f(x: pd.Series) -> pd.Series:
    if x.name == 'population' or x.name == 'region':
        return x
    else:
        return x / 1000

df = df.rename(columns={
    'gdp': 'gdp_trln'
})

print(df.apply(f, axis='index'))