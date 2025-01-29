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
'''
Series.apply(func, convert_dtype=True, args=(), **kwds)
Параметры:
    func:
        Это функция, которая будет применена к каждому элементу Series. Функция может быть встроенной, пользовательской или лямбда-функцией.
    convert_dtype:
        Булевый параметр (по умолчанию True). Если True, результат будет преобразован в наиболее подходящий тип данных. 
        Если False, возвращается тип данных, как есть.
    args:
        Кортеж, содержащий дополнительные аргументы, которые будут переданы в функцию func.
    kwds:
        Дополнительные именованные аргументы, которые также будут переданы в функцию func.
'''

'''
Метод isdigit() является встроенным методом строк в Python, который используется для проверки, 
состоит ли строка только из цифр. Он возвращает, если все символы в строке являются цифрами, и False` в противном случае.
str.isdigit(self)
    Параметры:
        self:
            Это строка, для которой вызывается метод. Метод не принимает дополнительных параметров.
    Возвращаемое значение:
        Метод возвращает:
            True: если все символы в строке являются цифрами (0-9) и строка не пуста.
            False: если строка содержит хотя бы один нецифровой символ или если строка пуста.
    Примечания:
        Метод isdigit() учитывает только символы, которые являются цифрами. 
        Например, он не распознает десятичные точки, знаки минус или пробелы как цифры.
        Метод работает с символами, которые представляют цифры в различных числовых системах 
        (например, арабские цифры, римские цифры и т.д.), но не распознает буквы или знаки.
'''
s_int = s.apply(lambda x: int(x) if str(x).isdigit() else None)
'''
# to_numeric():
    #Преобразует значения в числовой тип. Можно использовать параметр errors для обработки ошибок:
'''
'''
Метод pd.to_numeric() из библиотеки Pandas используется для преобразования аргумента (обычно Series или списка) 
в числовой тип данных. Этот метод может обрабатывать различные форматы чисел и предоставляет возможность управлять ошибками, 
возникающими при преобразовании.
pandas.to_numeric(arg, errors='raise', downcast=None)
    Параметры:
        arg:
            Это входные данные, которые Вы хотите преобразовать в числовой тип. Это может быть:
                Series
                Список
                Массив NumPy
                Индекс
                Другие структуры данных, содержащие числовые значения.
        errors:
            Опциональный параметр, который определяет, как обрабатывать ошибки при преобразовании. Возможные значения:
            'raise': (по умолчанию) выбрасывает исключение, если не удается преобразовать значение.
            'coerce': заменяет нечисловые значения на NaN.
            'ignore': возвращает исходные данные без изменений, если не удается преобразовать.
        downcast:
            Опциональный параметр, который позволяет указать, в какой тип данных следует преобразовать результат. Возможные значения:
            'integer': для преобразования в целочисленный тип.
            'float': для преобразования в тип с плавающей запятой.
            'string': для преобразования в строковый тип.
    Возвращаемое значение:
        Метод возвращает:
            Числовой тип данных (например, int, float) или Series, содержащий преобразованные значения. 
            Если указано errors='coerce', то нечисловые значения будут заменены на NaN.
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

'''
pandas.to_datetime(arg, 
                   errors='raise', 
                   dayfirst=False, 
                   yearfirst=False, 
                   utc=None, 
                   format=None, 
                   exact=False, 
                   unit=None, 
                   infer_datetime_format=False, 
                   origin='unix', 
                   cache=True)
Параметры:
    arg:
        Это основной аргумент, который может быть строкой, списком строк, массивом, 
        Series или DataFrame, содержащим даты или временные метки, которые нужно преобразовать.
    errors:
        Определяет, как обрабатывать ошибки, возникающие при преобразовании.
        'raise': выбрасывает ошибку, если преобразование не удалось (по умолчанию).
        'coerce': преобразует некорректные значения в NaT (Not a Time).
        'ignore': возвращает исходные значения, если преобразование не удалось.
    dayfirst:
        Если True, то день будет интерпретироваться первым в формате даты (например, DD/MM/YYYY).
    yearfirst:
        Если True, то год будет интерпретироваться первым в формате даты (например, YYYY/MM/DD).
    utc:
        Если True, возвращает временные метки в формате UTC. Если False, возвращает локальные временные метки.
    format:
        Позволяет указать формат входных данных. Например, можно использовать формат "%Y-%m-%d" для явного указания структуры даты.
    exact:
        Если True, то метод требует точного соответствия формата. Если False, то допускаются некоторые расхождения.
    unit:
        Указывает единицу времени, если входные данные представляют собой числовые значения 
        (например, 's' для секунд, 'ms' для миллисекунд и т.д.).
    infer_datetime_format:
        Если True, метод пытается автоматически определить формат даты и времени для улучшения производительности.
    origin:
        Определяет, откуда отсчитывать временные метки, если входные данные являются числовыми значениями. 
        Например, 'unix' означает, что отсчет начинается с 1 января 1970 года.
    cache:
        Если True, то использует кэш для улучшения производительности при повторном преобразовании одинаковых значений.                   
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
'''
pandas.to_timedelta(arg, unit=None, errors='raise')

Метод pd.to_timedelta() из библиотеки Pandas используется для преобразования аргумента (обычно строк, чисел или списков)
в тип данных timedelta, который представляет собой разницу между двумя временными моментами. Этот метод полезен для работы
с временными интервалами.
    Параметры:
        arg:
            Это входные данные, которые Вы хотите преобразовать в тип timedelta. Это может быть:
            Строка (например, '1 days', '2 hours', '3 minutes').
            Число (например, 5, что будет интерпретировано как 5 единиц времени в указанной единице).
            Список, массив или Series, содержащий значения, которые нужно преобразовать.
        unit:
            Опциональный параметр, который указывает единицу времени, если arg является числом. Возможные значения:
                'D': дни
                'h': часы
                'm': минуты
                's': секунды
                'ms': миллисекунды
                'us': микросекунды
                'ns': наносекунды
            Если arg уже является строкой, этот параметр игнорируется.

        errors:
            Опциональный параметр, который определяет, как обрабатывать ошибки при преобразовании. Возможные значения:
                'raise': (по умолчанию) выбрасывает исключение, если не удается преобразовать значение.
                'coerce': заменяет невалидные значения на NaT (Not a Time).
                'ignore': возвращает исходные данные без изменений, если не удается преобразовать.
Возвращаемое значение:
    Метод возвращает:
        Объект типа timedelta или Series, содержащий преобразованные временные интервалы.
'''
s_time = s.apply(lambda x: pd.to_timedelta(x, errors='coerce') if isinstance(x, str) and x.endswith('d') else None)


#convert_dtypes():
#Автоматически преобразует типы данных в DataFrame в более подходящие типы, такие как string, Int64, boolean и т.д.:
#df.convert_dtypes()

#replace():
#Можно использовать для замены значений в Series, что может быть полезно перед преобразованием типов:
'''
Series.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')

Метод s.replace() в библиотеке Pandas используется для замены значений в объекте Series или DataFrame. 
Этот метод позволяет заменять одно или несколько значений на другие, 
что может быть полезно для очистки данных или подготовки их к анализу.
    Параметры:
        to_replace:
            Значение или список значений, которые нужно заменить. Это может быть:
                Одно значение (например, 'old_value').
                Список значений (например, ['old_value1', 'old_value2']).
                Словарь, где ключи — это значения для замены, а значения — это новые значения 
                    (например, {'old_value': 'new_value'}).
        value:
            Значение или список значений, на которые нужно заменить to_replace. 
            Если to_replace является словарем, то этот параметр игнорируется.
        inplace:
            Логическое значение (по умолчанию False). Если установлено в True, 
            изменения будут применены непосредственно к исходному объекту, и метод не будет возвращать новый объект.
        limit:
            Целое число, указывающее максимальное количество замен, которые нужно выполнить. Если не указано, 
            будут заменены все вхождения.
        regex:
            Логическое значение (по умолчанию False). Если установлено в True, 
            to_replace будет интерпретироваться как регулярное выражение.
        method:
            Метод, используемый для замены значений. По умолчанию 'pad', что означает, 
            что замена будет происходить с использованием предыдущего значения. Другие варианты включают 'bfill' 
            (заполнение значениями вперед) и None.
Возвращаемое значение:
    Метод возвращает новый объект Series или DataFrame с замененными значениями, 
    если inplace=False. Если inplace=True, возвращается None.
'''
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
