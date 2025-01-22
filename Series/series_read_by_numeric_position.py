from pandas import Series
'''
    Чтение/выбор элементов серии по числовой позиции
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

# выбор по номеру позиции (устарело)
print(s[2])
print(s[3])

# выбрать по срезу и проверить равенство (не рекомендуется)
print(s[0:3])
