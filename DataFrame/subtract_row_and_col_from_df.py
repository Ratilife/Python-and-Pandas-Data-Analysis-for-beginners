from pandas import DataFrame

"""
Вычтите строку и столбец из dataframe
"""

stock_prices = DataFrame(data={
    'MSFT': [417, 416, 417, 420, 430],
    'IBM': [224, 222, 219, 221, 220],
    'AAPL': [225, 225, 226, 226, 233]
}, index=['2024-10-03', '2024-10-02', '2024-10-01', '2024-09-30', '2024-09-29'])

period_mean = stock_prices.mean(axis='rows')
company_daily_mean = stock_prices.mean(axis='columns')

print('\nЦены на акции:')
print(stock_prices)

print('\nСредние периоды цен:')
print(period_mean)

print('\nСредние ежедневные цены:')
print(company_daily_mean)
# [ ]
# [ ]
# [ ]
# [ ]
# -
# [ ]
print('\nПериод отклонения от среднего:')
print(stock_prices - period_mean)
# [ ]   [ ]
# [ ]   [ ]
# [ ] - [ ]
# [ ]   [ ]
print('\\nОтклонение от средних цен на компании:')
print(stock_prices.subtract(company_daily_mean, axis='rows'))


