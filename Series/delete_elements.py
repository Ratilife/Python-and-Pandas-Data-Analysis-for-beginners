from pandas import Series

# Удаление одного или нескольких ключей/значений из Series

# создание Series с использованием списков
gdp_regions = Series(data=[34931, 32095, 23125, 4043, 2722, 2028],
                     index=['Asia', 'North America', 'Europe', 'South America', 'Africa', 'Oceania'])
print('До:')
print(gdp_regions)
# добавление регионов
gdp_regions['Arctica'] = 5
gdp_regions['Antarctica'] = 12
assert 'Arctica' in gdp_regions.keys()

# удаление данных по одному ключу/значению
del gdp_regions['Oceania']
assert 'Oceania' not in gdp_regions.keys()

# Удалить несколько key/values
gdp_regions.drop(labels=['Antarctica', 'Arctica'], inplace=True)
assert 'Antarctica' not in gdp_regions.keys()
assert 'Arctica' not in gdp_regions.keys()
print('После:')
print(gdp_regions)