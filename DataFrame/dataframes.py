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

def get_regional_sales_data():
    df = DataFrame(
        data=[
            ['south', 'pc', 120, 73182],
            ['south', 'laptops', 150, 90873],
            ['south', 'tablets', 200, 65117],
            ['north', 'pc', 15, 71764],
            ['north', 'laptops', 18, 88234],
            ['north', 'tablets', 30, None],  # Нет данных по цене
            ['east', 'pc', 87, 71764],
            ['east', 'laptops', None, 89245],  # Нет данных по количеству
            ['east', 'tablets', 112, 63485],
            ['west', 'pc', 16, 72245],
            ['west', 'laptops', 23, 85123],
            ['west', 'tablets', 14, 53213]
        ],
        columns=['region', 'product', 'quantity', 'price']
    )
    df.index = df['region'] + '_' + df['product']
    return df
