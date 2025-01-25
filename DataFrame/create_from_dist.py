from pandas import DataFrame

# Создать из словаря

'''
    'course':
        Имя колонки
    ['math', 'statistics', 'economics', 'finance']
        значения строк
'''
economic_courses = DataFrame({
    'course': ['math', 'statistics', 'economics', 'finance'],
    'difficulty': [9, 8, 10, 9]
})

print('Экономические курсы:')
print(economic_courses)
