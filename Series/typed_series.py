from pandas import Series

s1 = Series(data=[1, 2, 3, 4, 5], index=list('abcde'))
s2 = Series(data=[10, 20, 30, 40, None, 60], index=list('abcdef'))
s3 = Series(data=['123', '234', '345', 456], index=list('abcd'))

print('\nСерия с значениями int')
print(s1)
print('\nСерия с одним значением.')
print(s2)
print('\nСерия всего:')
print(s2 + s2)
print('\nОбъектная серия:')
print(s3)  # Похоже, цифры в консоли, но тип - это объект
