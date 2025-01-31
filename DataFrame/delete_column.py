from pandas import DataFrame
'''
Удалить колонку
'''
# Создать из словаря
economic_courses = DataFrame({
    'course': ['math', 'statistics', 'economics', 'finance'],
    'students_subscribed': [100, 90, 95, 120],
    'difficulty': [9, 8, 10, 9],
    'teacher_rating': [10, 9, 5, 8]
})

economic_courses.set_index('course', inplace=True)

del economic_courses['teacher_rating']

print(economic_courses)
