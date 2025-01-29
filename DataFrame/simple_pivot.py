from sales_df import get_car_sales_df

# Print table
sales = get_car_sales_df()
sales_by_city = sales.pivot_table(values='sales', index='city', aggfunc='sum')

print('Total sales by city:')
print(sales_by_city)

print('Sales by city and car producer:')
sales_by_city_and_producer = sales.pivot_table(values='sales', index=['city', 'brand'], aggfunc=['sum', 'mean'])

print(sales_by_city_and_producer)