from pandas import DataFrame

def get_sales():
    return DataFrame(
        data={
            'quantity': [100, 123, 134, 56, 99, 64, 38, 98, 192, 283],
            'price': [12, 14, 18, 17, 19, 21, 20, 23, 19, 17],
            'discount': [0.01, 0.02, 0, 0, 0.03, 0.04, 0.05, 0.01, 0.015, 0.025]
        },
        index=['jan', 'feb', 'man', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct']
    )