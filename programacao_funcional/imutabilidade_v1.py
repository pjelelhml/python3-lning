#!/usr/local/bin/python3

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# setlocale(LC_ALL, 'pt_br')
# print(month_name)

meses_31 = filter(lambda mes: mdays[mes] > 30, range(1, 13))
nome_meses_31 = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
    nome_meses_31, ' Meses com 31 dias:')

print(juntar_meses)
