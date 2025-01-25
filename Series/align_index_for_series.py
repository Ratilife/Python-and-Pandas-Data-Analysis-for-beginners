from pandas import Series

usd_sales = Series(data=[112, 234, 345, 456], index=['jan', 'feb', 'mar', 'apr'])
rub_per_usd_rate = Series(data=[80, 81, 90, 85, 70, 87, 92, 95, 100, 98, 96, 99],
                         index=['jan', 'feb', 'mar', 'apr',
                                'may', 'jun', 'jul', 'aug',
                                'sep', 'oct', 'nov', 'dec'])

# Рассчитайте продажи в рублях
rub_sales = usd_sales * rub_per_usd_rate
print('Рублей sales:')
print(rub_sales)

print('\nРублевые продажи без NA:')
print(rub_sales.dropna())

# с Филлиной:
rub_sales_no_na = usd_sales.multiply(rub_per_usd_rate, fill_value=0)
print('\nПродажи рублей без NA:')
print(rub_sales_no_na)
