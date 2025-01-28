from pandas import Series
from dataframes import get_countries_gdp

# Применить функцию к столбцам DataFrame для создания другого столбца

def get_per_capita_gdp(country_row: Series,
                       currency: str | None = None,
                       ex_rate: str | None = None) -> float:
    per_capita = country_row['gdp'] / country_row['population']
    if currency == 'USD' or currency is None:
        return per_capita
    else:
        return per_capita * ex_rate

df = get_countries_gdp()

# apply function to each row
df['gdp_per_capita'] = df.apply(func=get_per_capita_gdp, axis='columns')

# provide additional parameters
df['gdp_per_capita_cur'] = df.apply(func=get_per_capita_gdp,
                                    axis='columns',
                                    currency='EUR',
                                    ex_rate=0.9)

print(df)