from pandas import Series

"""
    Выбор элементов из серии по условию
"""

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

# маска/состояние
condition = s > 10000
assert isinstance(condition, Series)
print(s[condition])

# сложное состояние
print('Countries with GDP between 2 and 20 trln USD:')
print(s[(s > 2000) & (s < 20000)])

# использование НЕ в условии
print('Other countries: use ~ operator')
print(s[~((s > 2000) & (s < 20000))])

# выбрать по числовому индексу: используйте iloc
print('Select by numeric index')
print(s.iloc[1:3])
