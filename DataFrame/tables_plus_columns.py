from pandas import DataFrame

"""
Применить функцию вдоль столбцов и рядов (axis)
"""

quarterly_financials = DataFrame(data=[
    [1788, 1932, 1954, 2413],
    [612, 749, 778, 594],
    [505, 580, 604, 508]
], columns=['1q', '2q', '3q', '4q'],
index=['Revenue', 'Operating income', 'Net income'])

total_by_year = quarterly_financials.sum(axis='columns')
as_pct_of_total = quarterly_financials.divide(total_by_year, axis='rows') * 100
as_pct_of_total['total'] = as_pct_of_total.sum(axis='columns')

print(quarterly_financials)
print('\nTotal by year:')
print(total_by_year)
print('\nAs percentage of total:')
print(as_pct_of_total)
print('\nRounded data:')
print(as_pct_of_total.round(2))
