# Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.
# EX: Digite um número: 1834
# - unidade: 4
# - Dezena: 3
# - Centena: 8
# - Milhar: 1

num = int(input('Informe um número de 0 até 9999: '))

print('Unidade: {}'.format(num % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000))