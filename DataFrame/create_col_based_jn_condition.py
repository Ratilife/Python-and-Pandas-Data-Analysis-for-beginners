from pandas import DataFrame

courses = DataFrame({
    'course': ['math', 'statistics', 'economics', 'finance', 'biology'],
    'difficulty': [9, 8, 10, 9, 7],
})

# создать новый столбец на основе условия:
courses.loc[courses['difficulty'] <= 8, 'level'] = "easy"
courses.loc[courses['difficulty'] > 8, 'level'] = "hard"

# обновить значение в столбце в зависимости от условия:
courses.loc[courses['level'] == 'hard', 'level'] = 'normal'

print(courses)