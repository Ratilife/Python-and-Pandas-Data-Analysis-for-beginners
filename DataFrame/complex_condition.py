from dataframes import get_countries_gdp
'''
    сложное условие
'''
# Получаем DataFrame с данными о странах
df = get_countries_gdp()
print(df)
# Выводим сообщение о странах с ВВП выше среднего
print('\nCountries with GDP more than average')
# Вычисляем средний ВВП
avg_gdp = df['gdp'].mean()
# Выводим средний ВВП, округленный до одного знака после запятой
print(f'Avg GDP is {round(avg_gdp, 1)} bn USD')

# Выводим сообщение о странах с ВВП выше среднего, исключая Арктику и Антарктику
print('\nCountries with GDP more than average except Arctica and Antarctica')
# Фильтруем DataFrame, чтобы получить страны с ВВП ниже среднего и не относящиеся к Арктике и Антарктике
real_countries = df[(df['gdp'] <= avg_gdp) & (df['region'] != 'Arctica')
                    & (df['region'] != 'Antarctica')]

# Альтернативный способ фильтрации с использованием булевых серий
# Создаем булеву серию для стран, не относящихся к Арктике и Антарктике
is_real_country = (df['region'] != 'Arctica') & (df['region'] != 'Antarctica')
# Создаем булеву серию для стран с ВВП ниже среднего
less_than_avg_gdp = df['gdp'] <= avg_gdp
# Фильтруем DataFrame, используя обе булевы серии
real_countries = df[less_than_avg_gdp & is_real_country]
# Выводим отфильтрованные страны
print(real_countries)
