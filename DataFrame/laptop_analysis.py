from pandas import read_csv
from pandas import ExcelWriter

# Read CSV-file with raw data,
# make calculations
# write results to different sheets of the same Excel file

curr_folder = './PandasBaseCourse/dataframe/read_analyze_write_to_excel/'
laptop_sales = read_csv(f'{curr_folder}/data/laptop_prices.csv')

# average sales price for each producer
avg_price_by_model = laptop_sales.groupby(by='Company')[['Price_euros']].mean()
avg_price_by_model.sort_values(by='Price_euros', ascending=False, inplace=True)
avg_price_by_model.rename(columns={'Price_euros': 'avg_price'}, inplace=True)

print('Average price by company')
print(avg_price_by_model)

count_of_laptops_by_type = laptop_sales.groupby(
    by='TypeName')[['Product']].count().sort_values(by='Product',
    ascending=False)
count_of_laptops_by_type.rename(columns={
    'Product': 'count_of_laptops'
}, inplace=True)
print('\nCount of laptops by type:')
print(count_of_laptops_by_type)

print('\nCount of laptops by type:')
print(count_of_laptops_by_type)

# save results to different sheets of the same Excel file
with ExcelWriter(f'{curr_folder}/result.xlsx') as writer:
    avg_price_by_model.to_excel(writer, sheet_name='avg_price')
    count_of_laptops_by_type.to_excel(writer, sheet_name='count_of_laptops')