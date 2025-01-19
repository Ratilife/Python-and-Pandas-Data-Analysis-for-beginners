from pandas import Series

"""
Различные способы создания сериалов
"""

# Создать серию, используя словарь
gdp_countries = Series(data={
    'USA': 28781,
    'Russia': 2056,
    'China': 18532,
    'South Korea': 1760,
    'France': 3130,
    'Germany': 4591,
    'UK': 3495,
    'Japan': 4110,
    'Canada': 2242
}, name='gdp_countries')

print('\nGDP for countries:')
print(gdp_countries)

# создавать серии, используя списки

gdp_regions = Series(data=[34931, 32095, 23125, 4043, 2722, 2028],
                     index=['Asia', 'North America', 'Europe', 'South America', 'Africa', 'Oceania'],
                     name='gdp_regions')

print('\nGDP for regions:')
print(gdp_regions)

