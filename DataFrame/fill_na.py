from dataframes import get_regional_sales_data

df = get_regional_sales_data()

print('\nRegional sales data:')
print(df)

no_na_df = df.fillna(value=0)
print('\nRegional sales data with no Na:')
print(no_na_df)
