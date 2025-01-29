from dfs import get_countries_gdp

"""
Создать новый столбец в цикле
"""

df = get_countries_gdp()

for country in df.index:
    current_gdp = df.loc[country, 'gdp']
    df.loc[country, 'gdp_trln'] = current_gdp / 1000
print(df)
