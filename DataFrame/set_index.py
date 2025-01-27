from pandas import DataFrame

# создать из словаря
economic_courses = DataFrame({
    'course': ['math', 'statistics', 'economics', 'finance'],
    'students_subscribed': [100, 90, 95, 120],
    'difficulty': [9, 8, 10, 9],
    'teacher_rating': [10, 9, 5, 8]
})

economic_courses.set_index('course', inplace=True)
print(economic_courses)
print('\nКоличество студентов, подписавшихся на курс статистики:')
print(economic_courses.loc['statistics', 'students_subscribed'])