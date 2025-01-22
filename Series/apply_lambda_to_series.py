from pandas import Series

"""
Примените функцию к каждому элементу, чтобы получить еще одну Series
"""

gdp_bln = Series(data={'USA': 28781,
                       'Russia': 2056,
                       'China': 18532,
                       'South Korea': 1760,
                       'France': 3130,
                       'Germany': 4591,
                       'UK': 3495,
                       'Japan': 4110,
                       'Canada': 2242})

gdp_as_pct = gdp_bln / gdp_bln.max() * 100

rounded_series = gdp_as_pct.apply(lambda x: f"{round(x, 2)}%")

print('Initial series:')
print(gdp_bln)

print('\n Series after apply')
print(rounded_series)
