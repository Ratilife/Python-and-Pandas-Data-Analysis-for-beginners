from dataframes import get_regional_sales_data
from pandas import isna

df = get_regional_sales_data()

# что такое Nan?
north_tablets_sales = df.query("region == 'north' & product == 'tablets'")
val = north_tablets_sales.loc['north_tablets', 'price']

print('Продажи планшетов в северном регионе:')
print(north_tablets_sales)

print('\nCheck if value is Nan')
print(val)
print(type(val))

# Проверка значения Nan
print(isna(val))
