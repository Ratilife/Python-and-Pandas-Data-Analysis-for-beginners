from pandas import Series

"""
Примените функцию к каждому элементу, чтобы получить еще одну Series
"""
# Создаем Series с данными о ВВП в миллиардах долларов для разных стран
gdp_bln = Series(data={'USA': 28781,
                       'Russia': 2056,
                       'China': 18532,
                       'South Korea': 1760,
                       'France': 3130,
                       'Germany': 4591,
                       'UK': 3495,
                       'Japan': 4110,
                       'Canada': 2242})
# Вычисляем ВВП каждой страны как процент от максимального ВВП в Series
gdp_as_pct = gdp_bln / gdp_bln.max() * 100
# Применяем функцию к каждому элементу, округляя значение до двух знаков после запятой и добавляя знак процента
rounded_series = gdp_as_pct.apply(lambda x: f"{round(x, 2)}%")
# Печатаем исходную Series с данными о ВВП
print('Initial series:')
print(gdp_bln)
# Печатаем новую Series с процентными значениями
print('\n Series after apply')
print(rounded_series)
