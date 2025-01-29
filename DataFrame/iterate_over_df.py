from dfs import get_countries_gdp

"""
Итерация над столбцами и рядами DataFrame
"""

df = get_countries_gdp()

# итерация над столбцами и рядами
for c in df.columns:
    for ind in df.index:
        current_value = df.loc[ind, c]
        print(f'Column = {c}, row = {ind}, value = {current_value}')
