#!/usr/local/bin/python3

# funcao calcular conhece o valor de x pois está na vizinhança
def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(2)}')