# merge_df.py

from pandas import DataFrame
import pandas as pd

# initialize test results
test_results = DataFrame(data=[
  [1, 'math', 'ivan', 5],
  [2, 'chem', 'peter', 4],
  [3, 'bio', 'nick', 5],
  [4, 'hist', 'kate', 4]
], columns=['key', 'course_id', 'student_id', 'grade'])

# initialize courses
courses = DataFrame(data=[
  ['math', 'Mathematics'],
  ['chem', 'Chemistry'],
  ['bio', 'Biology'],
  ['hist', 'History']
], columns=['course_id', 'course_name'])
courses.set_index('course_id', inplace=True)

students = DataFrame(data=[
    ['ivan', 'Иван'],
    ['peter', 'Петр'],
    ['nick', 'Николай'],
    ['kate', 'Екатерина']
], columns=['student_id', 'student_name'])

print('Test results:')
print(test_results)

print('Test results:')
print(test_results)

print('\nCourses:')
print(courses)

print('\nStudents:')
print(students)

print('\nJoin students to test results')
test_results_with_students = pd.merge(left=test_results,
    right=students,
    left_on='student_id',
    right_on='student_id',
    how='inner')

print(test_results_with_students)

print('\nJoin with courses:')
final_results = pd.merge(left=test_results_with_students,
    right=courses,
    left_on='course_id',
    left_index=False,
    right_index=True,
    how='inner')
print(final_results)
