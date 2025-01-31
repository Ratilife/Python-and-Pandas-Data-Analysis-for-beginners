from pandas import DataFrame
'''
Преобразование целово числа в число с плавающей точкой
'''
df = DataFrame(
    index=['USA', 'Russia', 'China', 'South Korea', 'France', 'Germany', 'UK', 'Japan', 'Canada'],
    data={
        'gdp': [28781, 2056, 18532, 1760, 3130, 4591, 3495, 4110, 2242],
        'population': [335.8, 146.1, 1409.6, 51.2, 68.4, 84.673, 67.5, 123.8, 15.18]
    }
)

# преобразовать в миллиарды
new_df = df.apply(lambda x: round(x / 1000, 2))
print('DataFrame раньше:')
print(df)

print('DataFrame за миллиарды:')
print(new_df)