from pandas import Series
'''
    Сократите ряд до одного значения, применив функцию к series
        ex. min, max, avg, median
'''

gdp_bln = Series(data={'USA': 28781,
                       'Russia': 2056,
                       'China': 18532,
                       'South Korea': 1760,
                       'France': 3130,
                       'Germany': 4591,
                       'UK': 3495,
                       'Japan': 4110,
                       'Canada': 2242})
max_gdp = gdp_bln.max()
mean_gdp = gdp_bln.mean()
median_gdp = gdp_bln.median()
print(f'Max GDP is {max_gdp}, \n' +
      f'Average GDP is {mean_gdp}, \n' +
      f'Median GDP is {median_gdp}')

# express each element as % of max value
gdp_as_pct = gdp_bln / gdp_bln.max() * 100
print(gdp_as_pct)
