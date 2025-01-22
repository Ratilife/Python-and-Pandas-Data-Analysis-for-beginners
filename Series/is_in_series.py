from pandas import Series

"""
Проверьте, находится ли элемент в коллекции ключей/значений серии.
"""

# создавать серии, используя списки
gdp_regions = Series(data=[34931, 32095, 23125, 4043, 2722, 2028],
                     index=['Asia', 'North America', 'Europe',
                            'South America', 'Africa', 'Oceania'])

# утверждать, что ключ находится в коллекции ключей
assert 'Asia' in gdp_regions.keys()

# утверждать значения находится в коллекции значений
assert 34931 in gdp_regions.values
