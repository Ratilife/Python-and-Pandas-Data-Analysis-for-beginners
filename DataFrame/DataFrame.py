#DataFrame - таблицы. Состоит из Series
from pandas import DataFrame
df = DataFrame(index=['USA', 'Russia', 'China'],
               data={
                   'gdp': [28781, 2056, 18532],
                   'population': [335.8, 146.1, 1409.6],
                   'region': ['America', 'Europe', 'Asia']
               })
