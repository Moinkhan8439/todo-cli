from os import get_terminal_size
import sys
import os
from datetime import datetime
def getLine():
    for _ in range(get_terminal_size().columns//2):
            print('#',end="")

def getQuote():
    return ("Yesterday i was clever i wanted to change the world. Today i am wise i am changing myself")


def exit():
    os.system("clear")
    sys.exit()

def getDate():
    month=datetime.today().strftime("%B")
    return ''.join([str(datetime.today().day),"-",str(month[:3]),"-",str(datetime.today().year)])


def validate(date):
    try:
        day, month, year=date.split('-')
        day,month,year=int(day),int(month),int(year)
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year%4==0 and (year%100 != 0 or year%400==0):
            day_count_for_month[2] = 29
    except ValueError:
        return None
    return date if(1 <= month <= 12 and 1 <= day <= day_count_for_month[month]) else ( None) 
