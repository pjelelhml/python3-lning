#!/usr/local/bin/python3

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Joana', 'idade': 16},
    {'nome': 'Rebeca', 'idade': 12},
    {'nome': 'Gabriela', 'idade': 17},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Mariana', 'idade': 26},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))
print(f'-' * 60)
nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nomes_grandes))