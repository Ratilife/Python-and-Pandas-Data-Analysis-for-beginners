from pandas import read_csv
'''
Описание
    read_csv() — это функция, используемая для чтения данных из CSV (Comma-Separated Values) 
    файла и преобразования их в объект DataFrame.

Параметры
    filepath_or_buffer: str, path object, или file-like object
        Путь к файлу или объект, который поддерживает чтение.
    sep: str, по умолчанию ','
        Разделитель, используемый в файле. Например, sep='\t' для табуляции.
    header: int, list of int, или None, по умолчанию 'infer'
        Строка (или список строк), используемая в качестве заголовка.
        Если None, заголовок не будет использоваться.
    names: array-like, по умолчанию None
        Список имен столбцов. Если указано, заголовок будет проигнорирован.
    skiprows: list-like, int, или None, по умолчанию None
        Строки, которые нужно пропустить в начале файла.
    na_values: scalar, str, list-like, или dict, по умолчанию None
        Значения, которые будут интерпретироваться как NaN.
    true_values: list, по умолчанию None
        Значения, которые будут интерпретироваться как True.
    false_values: list, по умолчанию None
        Значения, которые будут интерпретироваться как False.
    skipinitialspace: bool, по умолчанию False
        Пропускать пробелы после разделителей.
    convert_dates: bool или list, по умолчанию True
        Преобразовывать столбцы в даты.
    encoding: str, по умолчанию None
        Кодировка файла. Например, 'utf-8'.
    error_bad_lines: bool, по умолчанию True
        Пропускать строки с ошибками.
    warn_bad_lines: bool, по умолчанию True
        Выводить предупреждения о строках с ошибками.
Возвращаемое значение
DataFrame: Объект DataFrame, содержащий данные из CSV файла.
'''
# путь к файлу
file_path = 'F:/Языки/Python/UChoba/Анализ данных на Python и Pandas/Analiz_dannix_Pandas/files/33_96_many_chl_20240918.csv'

# чтение файла
laptop_prices = read_csv(file_path, delimiter=';')
print(laptop_prices)
print(laptop_prices.head())
