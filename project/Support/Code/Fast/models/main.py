from datetime import datetime


def show_date(date: datetime):
    today, month = date.day, date.month
    adapt = lambda value: value if value >= 10 else f'0{value}'
    
    return f'{adapt(today)}/{adapt(month)}'

