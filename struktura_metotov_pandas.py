import pandas as pd
data =filepath = n= df = s = value = df1=df2= query= connection=func=tuples=start=end=other=url=None
#1. Создание объектов
pd.Series(data)             #- создание одномерного массива.
pd.DataFrame(data)          #- создание двумерной таблицы.
pd.read_csv(filepath)       #- чтение данных из CSV файла.
pd.read_excel(filepath)     #- чтение данных из Excel файла.
#2. Основные операции с данными
df.head(n)                  #- получение первых n строк.
df.tail(n)                  #- получение последних n строк.
df.info()                   #- получение информации о DataFrame.
df.describe()               #- получение статистики по числовым столбцам.
#3. Индексация и выбор данных
df.loc[n]                   #- доступ по меткам.
df.iloc[n]                  #- доступ по индексам.
df.at[n]                    #- доступ к отдельному элементу по метке.
df.iat[n]                   #- доступ к отдельному элементу по индексу.
#4. Фильтрация данных
df[df['column'] > value]    #- фильтрация по условию.
df.query('condition')       #- фильтрация с использованием выражений.
#5. Обработка данных
df.drop(columns=['col1', 'col2'])           #- удаление столбцов.
df.fillna(value)                            #- заполнение пропусков.
df.dropna()                                 #- удаление строк с пропусками.
df.rename(columns={'old_name': 'new_name'}) #- переименование столбцов.
#6. Группировка и агрегация
df.groupby('column')                        #- группировка данных.
df.agg({'col1': 'sum', 'col2': 'mean'})     #- агрегация данных.
df.transform(func)                          #- применение функции к каждой группе и возврат результата в исходный размер.
#7. Слияние и объединение
pd.merge(df1, df2, on='key')                #- объединение двух DataFrame по ключу.
pd.concat([df1, df2])                       #- конкатенация DataFrame.
pd.join(other)                              #- объединение с другим DataFrame по индексу.
#8. Ввод и вывод данных
df.to_csv(filepath)                         #- запись DataFrame в CSV файл.
df.to_excel(filepath)                       #- запись DataFrame в Excel файл.
#9. Визуализация
df.plot()                                   #- базовая визуализация данных.
df.hist()                                   #- построение гистограммы.
df.boxplot()                                #- построение коробчатой диаграммы.
#10. Работа с временными рядами
pd.to_datetime()                            #- преобразование строк в формат даты и времени.
df.resample('M')                            #- изменение частоты временного ряда (например, на месячную).
df.shift(periods=1)                         #- сдвиг временного ряда на заданное количество периодов.
#11. Работа с категориальными данными
df.astype('category')                       #- преобразование столбца в категориальный тип.
df.cat.codes                                #- получение кодов категориальных данных.
df.cat.categories                           #- получение уникальных категорий.
#12. Работа с текстовыми данными
df.str.contains('substring')                #- проверка наличия подстроки в строках.
df.str.split('delimiter')                   #- разделение строк по разделителю.
df.str.replace('old', 'new')                #- замена подстроки в строках.
#13. Пивотирование и сводные таблицы
df.pivot(index='index_col', columns='columns_col',
       values='values_col')                 #- создание сводной таблицы.
df.pivot_table(values='values_col', index='index_col',
             columns='columns_col', aggfunc='mean')         #- создание сводной таблицы с агрегацией.
#14. Удаление дубликатов
df.drop_duplicates()                        #- удаление дублирующихся строк.
df.duplicated()                             #- проверка на наличие дубликатов.
#15. Применение функций
df.apply(func)                              #- применение функции к строкам или столбцам.
df.map(func)                                #- применение функции к элементам Series.
df.applymap(func)                           #- применение функции ко всем элементам DataFrame.
#16. Сортировка данных
df.sort_values(by='column', ascending=True) #- сортировка по значению столбца.
df.sort_index(ascending=True)               #- сортировка по индексу.
#17. Работа с NaN и пропущенными значениями
df.isna()                                   #- проверка на NaN.
df.notna()                                  #- проверка на неналичие NaN.
df.interpolate()                            #- интерполяция пропущенных значений.
#18. Статистические методы
df.mean()                                   #- среднее значение.
df.median()                                 #- медиана.
df.std()                                    #- стандартное отклонение.
df.corr()                                   #- корреляция между столбцами.
#19. Экспорт и импорт данных
pd.read_json(filepath)                      #- чтение данных из JSON файла.
df.to_json(filepath)                        #- запись DataFrame в JSON файл.
pd.read_sql(query, connection)              #- чтение данных из базы данных SQL.
#20. Работа с MultiIndex
pd.MultiIndex.from_tuples(tuples)           #- создание многоуровневого индекса.
df.set_index(['col1', 'col2'])              #- установка многоуровневого индекса.
df.unstack()                                #- преобразование многоуровневого индекса в столбцы.
#21. Работа с временными метками
df.dt                                       #- доступ к атрибутам временных меток (например, .dt.year, .dt.month, .dt.day).
df.date_range(start, end, freq='D')         #- создание диапазона дат.
#22. Работа с HTML
pd.read_html(url)                           #- чтение таблиц из HTML страницы.
df.to_html(filepath)                        #- запись DataFrame в HTML файл.
#23Оптимизация памяти
pd.to_numeric() #- преобразование столбца в числовой тип с возможностью обработки ошибок.