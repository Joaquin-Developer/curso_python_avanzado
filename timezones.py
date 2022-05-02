"""
- manejo de zonas horarias
"""
from datetime import datetime
import pytz


def timezone_example():
    """ejemplos de zonas horarias"""
    montevideo_timezone = pytz.timezone("America/Montevideo")
    montevideo_date = datetime.now(tz=montevideo_timezone)
    print("Montevideo: " + montevideo_date.strftime("%d/%m/%Y, %H:%M:%S"))


if __name__ == "__main__":
    timezone_example()
