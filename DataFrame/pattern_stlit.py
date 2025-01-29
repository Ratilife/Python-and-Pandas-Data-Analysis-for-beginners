from fio_df import get_employees_confused_data

"""
    Расколоть с помощью регулярных выражений
"""

df = get_employees_confused_data()
# data example:
# Прохоров  ,  Фёдор  Артурович - many spaces and even comma
# Егоров ,Матвей, Викторович - names are split by commas and whitespaces
#

splitted_df = df['fio'].str.split(pat=r'\s*,+\s*|\s+', expand=True)
splitted_df.columns = ['last_name', 'middle_name', 'first_name']

print(splitted_df)
