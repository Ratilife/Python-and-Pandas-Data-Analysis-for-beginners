from dfs import get_sales

"""
Excel-like calculations in pandas
"""

sales = get_sales()
print('Initial dataframe:')
print(sales)

# рассчитать прибыль
sales['profit'] = sales['quantity'] * sales['price']

# Рассчитайте прибыль после скидок:
sales['price_after_discount'] = sales['price'] * (1 - sales['discount'])
sales['profit_after_discount'] = sales['price_after_discount'] * sales['quantity']

rub_per_usd_rate = 90
sales['profit_rub_tsd'] = sales['profit'] * rub_per_usd_rate / 1000

print('\nDataFrame with new columns:')
print(sales)

total_profit = sales['profit'].sum()
after_discount_profit = sales['profit_after_discount'].sum()

print(f'\nTotal profit before discount = {total_profit}, ' +
      f'after discount = {after_discount_profit}')