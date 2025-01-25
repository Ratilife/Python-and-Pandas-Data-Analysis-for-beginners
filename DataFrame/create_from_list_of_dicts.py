from pandas import DataFrame

# Создать из списка словари:
physics_courses = DataFrame(data=[
    {'course': 'mechanics', 'difficulty': 8},
    {'course': 'thermodynamics', 'difficulty': 9},
    {'course': 'optics', 'difficulty': 9}
])

print('\nPhysics courses:')
print(physics_courses)
