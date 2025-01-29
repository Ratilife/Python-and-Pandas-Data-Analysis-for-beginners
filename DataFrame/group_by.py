from dataframes import get_countries_gdp

"""
    Самый простой пример Group_by
"""
df = get_countries_gdp()
df = df.sort_values(by=['region', 'population'], ascending=[True, False])
# group_by:
total_region_gdp = df.groupby(by='region').sum()
avg_region_gdp = df.groupby(by='region').agg('mean')

print('Initial dataframe:')
print(df)

print('GDP for regions:')
print(total_region_gdp)

print(f'\nAverage GDP:')
print(avg_region_gdp)