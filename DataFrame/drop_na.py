from dataframes import get_regional_sales_data
from pandas import isna

df = get_regional_sales_data()
no_na_df = df.dropna() # subset=['price']
# no_na_df = df.dropna(subset=['price'])
print(f'Initial dataframe of len = {len(df)}')
print(df)

print(f'\nNo NA dataframe of len = {len(no_na_df)}:')
print(no_na_df)
