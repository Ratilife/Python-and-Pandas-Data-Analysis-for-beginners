from pandas import DataFrame

def get_sales():
    return DataFrame(
        data={
            'quantity': [100, 123, 134, 56, 99, 64, 38, 98, 192, 283],
            'price': [12, 14, 18, 17, 19, 21, 20, 23, 19, 17],
            'discount': [0.01, 0.02, 0, 0, 0.03, 0.04, 0.05, 0.01, 0.015, 0.025]
        },
        index=['jan', 'feb', 'man', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct']
    )

def get_countries_gdp() -> DataFrame:
    df = DataFrame(
        index=['USA', 'Russia', 'China', 'South Korea',
               'France', 'Germany', 'UK', 'Japan', 'Canada', 'Antarctica', 'Arctica'],
        data={
            'gdp': [28781, 2856, 18532, 1760, 3130, 4591, 3495, 4110, 2242, 0, 0],
            'population': [335.8, 146.1, 1409.6, 51.2, 68.4, 84.673, 67.5, 123.8, 37.6, 0, 0],
            'region': ['America', 'Europe', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe',
                       'Asia', 'America', 'Antarctica', 'Arctica']
        }
    )
    return df
