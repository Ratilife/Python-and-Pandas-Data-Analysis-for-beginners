from pandas import DataFrame
def get_countries_gdp() -> DataFrame:
    df = DataFrame(
        index=['USA', 'Russia', 'China', 'South Korea', 'France', 'Germany', 'UK', 'Japan', 'Canada', 'Antarctica', 'Arctica'],
        data={
            'gdp': [28781, 2056, 18532, 1760, 3130, 4591, 3495, 4110, 2242, 0, 0],
            'population': [335.8, 146.1, 1409.6, 51.2, 68.4, 84.673, 67.5, 123.8, 38.01, 0, 0],
            'region': ['America', 'Europe', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Asia', 'America', 'Antarctica', 'Arctica']
        }
    )
    return df
