from dataframes import get_countries_gdp

#  Выбрать из фрейма данных, используя индекс(ы) и столбец(и)

df = get_countries_gdp()

print('GDP dataframe:')
print(df)

# Получите несколько рядов и столбцов:
print('\nGet USA, Russia and China GDP, population:')
top_countries = df.loc[['USA', 'Russia', 'China'], ['gdp', 'population']]
print(top_countries)

# используйте срезы для отображения диапазона строк и столбцов:
print('\nDisplay european countries:')
european_countries = df.loc['France':'UK', 'gdp':'population']
print(european_countries)