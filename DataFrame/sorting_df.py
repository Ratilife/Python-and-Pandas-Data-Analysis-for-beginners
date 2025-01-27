from dataframes import get_countries_gdp

# Сортировать DataFrame с использованием нескольких столбцов

df = get_countries_gdp()
print('Initial dataframe:')
print(df)

df = df.sort_values(by=['gdp', 'population'], ascending=False)

print('\nSorted values:')
print(df)