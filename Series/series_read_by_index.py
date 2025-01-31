from pandas import Series
'''
Series считываемая по индексу
'''
s = Series(data={
    'USA': 28781,
    'Russia': 2056,
    'China': 18532,
    'South Korea': 1760,
    'France': 3130,
    'Germany': 4591,
    'UK': 3495,
    'Japan': 4110,
    'Canada': 2242
})

# выберите одно значение
print(s['USA'])

# выберите только некоторые значения
print(s[['USA', 'China', 'Russia']])

# используйте атрибут loc для выбора подмножества значений
#Эта строка кода проверяет, что значения, полученные из Series s для индексов 'USA', 'China' и 'Russia', совпадают с ожидаемыми значениями.
assert s.loc[['USA', 'China', 'Russia']].equals(
    Series(index=['USA', 'China', 'Russia'], data=[28781, 18532, 2056])
)
