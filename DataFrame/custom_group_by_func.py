from pandas import DataFrame
from dataframes import get_countries_gdp

# custom function in group_by

df = get_countries_gdp()
df = df.sort_values(by=['region', 'population'], ascending=[True, False])

def f(region_data: DataFrame):
    return max(region_data['population'])

# group_by:
region_max_population = df.groupby(by='region')[['population']].apply(f)

# sort results:
region_max_population.sort_values(inplace=True, ascending=False)
print('All data:')
print(df)
print('\nMax population for each region:')
print(region_max_population)
