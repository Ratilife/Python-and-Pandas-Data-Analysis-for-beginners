from pandas import Series

"""
Добавить элементы в серию (так же, как в словарь)
"""

# создавать серии, используя списки
gdp_regions = Series(data=[34931, 32095, 23125, 4043, 2722, 2028],
                     index=['Asia', 'North America', 'Europe',
                            'South America', 'Africa', 'Oceania'])

gdp_regions['Antarctica'] = 1
gdp_regions['Arctica'] = 5
print(gdp_regions)

print('Value for Antarctica:')
print(gdp_regions['Antarctica'])
