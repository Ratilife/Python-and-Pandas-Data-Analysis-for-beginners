from pandas import Index, DataFrame
from pandas import concat
'''
объединение и повторный индекс
'''
winter_index = Index(data=['dec', 'jan', 'feb'])
summer_index = Index(data=['jun', 'ju', 'aug'])
year_index = Index(data=['jan', 'feb', 'man',
    'apr', 'may', 'jun',
    'ju', 'aug', 'sep',
    'oct', 'nov', 'dee'])

winter_sales = DataFrame(
    index=winter_index,
    data={'sales': [100, 200, 300],
    'profit': [10, 20, 30]}
)

summer_sales = DataFrame(
    index=summer_index,
    data={'sales': [10, 20, 30],
    'profit': [1, 2, 3]}
)
result = concat(objs=[winter_sales, summer_sales])
result = result.reindex(year_index)

print(result)