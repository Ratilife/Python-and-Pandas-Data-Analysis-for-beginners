from pandas import Series
from dataframes import get_countries_gdp

"""
Выберите из DataFrame, используя
простое условие для столбца
"""

df = get_countries_gdp()
print('Dataframe:')
print(df)

print('\nCountries with GDP less than average')
assert isinstance(df['gdp'], Series)
avg_gdp = df['gdp'].mean()
print(f'Avg GDP is {round(avg_gdp, 1)} bn USD')
filtered_df = df[df['gdp'] <= avg_gdp]
print(filtered_df)
