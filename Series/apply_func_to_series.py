from pandas import Series
'''
     Примените функцию к каждому элементу, чтобы получить другой series
'''
# Создаем Series с данными о ВВП в миллиардах долларов для разных стран
gdp_bln = Series(data={'USA': 28781,
                       'Russia': 2056,
                       'China': 18532,
                       'South Korea': 1760,
                       'France': 3130,
                       'Germany': 4591,
                       'UK': 3495,
                       'Japan': 4110,
                       'Canada': 2242})

def convert(usd_value: float,
            currency: str,
            exchange_rates: dict[str, float]) -> float:
    """
        Конвертирует значение в долларах США в указанную валюту
        на основе предоставленных курсов обмена.

        :param usd_value: Значение в долларах США, которое нужно конвертировать.
        :param currency: Код валюты, в которую нужно конвертировать (например, 'EUR', 'GBP').
        :param exchange_rates: Словарь, содержащий курсы обмена для различных валют.
        :return: Конвертированное значение в указанной валюте.
        """
    if currency not in exchange_rates.keys():
        # Проверяем, существует ли указанная валюта в словаре курсов обмена.
        raise Exception(f'{currency} not exists') # Если нет, выбрасываем исключение.
    ex_rate = exchange_rates[currency] # Получаем курс обмена для указанной валюты.
    return usd_value / ex_rate # Возвращаем конвертированное значение.

# Применяем функцию convert к каждому элементу Series gdp_bln,
# конвертируя значения в евро с использованием заданных курсов обмена.
print('\nConvert using exchange rate:')
converted_gdp = gdp_bln.apply(func=convert,
                              currency='EUR',
                              exchange_rates={
                                  'GBP': 1.1,
                                  'EUR': 1.23})
# Печатаем конвертированные значения ВВП в евро
print(converted_gdp)
