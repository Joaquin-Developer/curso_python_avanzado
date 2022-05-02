"""
- manejo de fechas con datetime
"""
import datetime


def dates():
    """ Fecha y hora actual del pc OR fecha UTC"""
    my_time = datetime.datetime.now()
    print(my_time)
    # día actual:
    today = datetime.date.today()
    print(today)
    print(f"Year: {today.year}")
    print(f"Month: {today.month}")
    print(f"Day: {today.day}")


def formatos_fechas():
    """ejemplos de formateo de fechas"""
    today = datetime.date.today()
    formateo = datetime.date.strftime(today, "%Y-%m-%d") # YYYY-MM-DD
    print(formateo)


if __name__ == "__main__":
    dates()
