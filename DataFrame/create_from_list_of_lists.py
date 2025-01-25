from pandas import DataFrame

# создание DataFrame из списка списков
math_courses = DataFrame(data=[
    ['linear algebra', 9],
    ['geometry', 10],
    ['calculus', 10]
], columns=['course', 'difficulty'])

print('\nMath courses:')
print(math_courses)
