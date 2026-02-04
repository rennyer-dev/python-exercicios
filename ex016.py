# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
# porção inteira. EX: 6.127 -> O número 6.127 tem a parte inteira 6
from math import trunc

numero = float(input('Informe um número quebrado: '))
parte_inteira = trunc(numero)

print('O número {} tem a parte inteira {}'.format(numero, parte_inteira))