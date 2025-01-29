from fio_df import get_employees

"""
Разделитель строкового столбца с использованием пробела 
и поместите разделенные части в разные столбцы
"""

df = get_employees()
names_df = df['fio'].str.split(pat=' ', expand=True)

names_df.columns = ['first_name', 'middle_name', 'last_name']

print(names_df)
