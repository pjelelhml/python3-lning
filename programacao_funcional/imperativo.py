#!/usr/local/bin/python3

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


print('Meses com 31 dias:')

for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')