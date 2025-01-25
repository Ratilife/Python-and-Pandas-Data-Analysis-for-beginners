import pandas as pd

# Создание Series с строковыми значениями и заданными индексами
s = pd.Series(['123', '234', '345', 456, 'old_value', '2023-01-01', '2023-01-02'],
              index=['a', 'b', 'c', 'd','e', 'f','g'])

# Вывод типа данных Series

print(s.dtype)
'''astype():
    # Преобразование Series в целочисленный тип
    # Используется для преобразования типов данных.
    # Например, s.astype('float64') для преобразования в тип с плавающей запятой.
#s_int = s.astype('int64')
'''
# Преобразование Series в целочисленный тип, обрабатывая только числовые значения
'''
    Использован метод apply() с лямбда-функцией, которая проверяет,
    является ли значение числом с помощью str(x).isdigit(). 
    Если значение похоже на число, оно преобразуется в int, в противном случае возвращается None.
'''
s_int = s.apply(lambda x: int(x) if str(x).isdigit() else None)
'''
# to_numeric():
    #Преобразует значения в числовой тип. Можно использовать параметр errors для обработки ошибок:
'''
s_num = pd.to_numeric(s, errors='coerce')  # Преобразует, заменяя нечисловые значения на NaN

# Преобразование в целочисленный тип, заменяя NaN на 0 или другой подходящий вариант
s_int = s_num.fillna(0).astype('int64')  # Заменяем NaN на 0 перед преобразованием
'''
#to_datetime():
#Преобразует строки в тип данных datetime. Это полезно для работы с временными данными:
s_date = pd.to_datetime(s)
'''
# Преобразование строк в тип данных datetime, обрабатывая только даты
'''
    Использован метод apply() с лямбда-функцией, которая проверяет, 
    является ли значение строкой и соответствует ли формату даты 
    (например, длина строки 10 символов и наличие дефисов в нужных позициях).
    Если значение похоже на дату, оно преобразуется с помощью pd.to_datetime(), 
    в противном случае возвращается None.
'''
'''
Объяснение:
    s.apply(...):
        Метод apply() применяется к объекту s, который является Series из библиотеки Pandas. 
        Этот метод позволяет применить функцию ко всем элементам Series.
    lambda x: ...:
        Здесь мы используем лямбда-функцию, которая принимает один аргумент x. 
        Эта функция будет применена к каждому элементу s.
    isinstance(x, str):
        Проверяет, является ли x строкой. 
        Это важно, потому что мы хотим обрабатывать только строковые значения.
    len(x) == 10:
        Проверяет, имеет ли строка длину 10 символов. 
        Это условие помогает убедиться, что строка может соответствовать формату даты YYYY-MM-DD, 
        который также имеет длину 10 символов.
    x[4] == '-' and x[7] == '-':
        Эти условия проверяют, находятся ли дефисы на правильных позициях в строке. 
        В формате даты YYYY-MM-DD дефис должен быть на 5-й и 8-й позициях (индексация начинается с 0). 
        Это помогает убедиться, что строка имеет правильный формат.
    pd.to_datetime(x, errors='coerce'):
        Если все предыдущие условия выполнены, строка x преобразуется в объект типа datetime с помощью функции pd.to_datetime().
        Параметр errors='coerce' означает, что если преобразование не удастся 
        (например, если строка не является корректной датой), 
        то будет возвращено значение NaT (Not a Time).
    else None:
        Если хотя бы одно из условий не выполнено (например, если x не строка или не соответствует формату даты), 
        то функция возвращает None.
Результат:
    В результате выполнения этой строки кода, s_date будет содержать:
    Даты, преобразованные в формат datetime, если строка соответствует формату YYYY-MM-DD.
    None для всех остальных значений, которые не соответствуют этому формату.
'''

s_date = s.apply(lambda x: pd.to_datetime(x, errors='coerce')
    if isinstance(x, str) and len(x) == 10
       and x[4] == '-' and x[7] == '-' else None)
'''
#to_timedelta():
#Преобразует строки в тип данных timedelta, который используется для представления разницы между датами:
s_time = pd.to_timedelta(s)
'''
'''
Объяснение:
    s.apply(...):
        Метод apply() применяется к объекту Series (в данном случае s). 
        Он позволяет применить функцию к каждому элементу Series.
    lambda x: ...:
        Это анонимная функция (лямбда-функция), которая принимает один аргумент x. 
        В данном контексте x представляет собой каждый элемент Series.
    isinstance(x, str):
        Эта проверка определяет, является ли элемент x строкой (str). 
        Это важно, потому что мы хотим обрабатывать только строковые значения.
    x.endswith('d'):
        Эта проверка определяет, заканчивается ли строка x на букву 'd'. 
        Это условие может использоваться для фильтрации строк, которые представляют собой временные интервалы 
            (например, '5d' для 5 дней). 
        Если строка не заканчивается на 'd', то она не будет обработана.
    pd.to_timedelta(x, errors='coerce'):
        Если оба условия (что x является строкой и заканчивается на 'd') выполняются, 
        то выполняется преобразование x в тип timedelta с помощью функции pd.to_timedelta(). 
        Параметр errors='coerce' указывает, что если преобразование не удастся 
            (например, если строка не может быть интерпретирована как временной интервал), 
        то будет возвращено значение NaT (Not a Time).
    else None:
        Если одно из условий не выполняется (то есть x не является строкой или не заканчивается на 'd'), 
        то функция возвращает None. Это означает, что для таких значений в результирующем Series будет записано None.
Результат:
    В результате выполнения этого кода s_time будет содержать новый Series, в котором:
    Элементы, которые являются строками и заканчиваются на 'd', будут преобразованы в тип timedelta.
    Все остальные элементы будут заменены на None.
'''
# Фильтрация и преобразование в timedelta
s_time = s.apply(lambda x: pd.to_timedelta(x, errors='coerce') if isinstance(x, str) and x.endswith('d') else None)


#convert_dtypes():
#Автоматически преобразует типы данных в DataFrame в более подходящие типы, такие как string, Int64, boolean и т.д.:
#df.convert_dtypes()

#replace():
#Можно использовать для замены значений в Series, что может быть полезно перед преобразованием типов:
s_rep = s.replace({'old_value': 'new_value'})

#apply():
#Позволяет применять произвольные функции к элементам Series или DataFrame, что может быть полезно для кастомного преобразования
#s.apply(lambda x: int(x))



# Вывод преобразованного Series
print(s_int)
print(s_num)
print(s_date)
print(s_time)
print(s_rep)
