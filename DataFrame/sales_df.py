from pandas import DataFrame
def get_car_sales_df():
    return DataFrame(data=[
        # moscow haval
        ['Moscow', 'jan', 'Haval', 1300],
        ['Moscow', 'feb', 'Haval', 1200],
        ['Moscow', 'mar', 'Haval', 1100],
        #
        # moscow cherry
        ['Moscow', 'jan', 'Chery', 800],
        ['Moscow', 'feb', 'Chery', 700],
        ['Moscow', 'mar', 'Chery', 600],
        #
        # moscow geely
        ['Moscow', 'jan', 'Geely', 2501],
        ['Moscow', 'feb', 'Geely', 2401],
    ], columns=['city', 'month', 'brand', 'sales'])