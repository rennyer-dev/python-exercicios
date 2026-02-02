# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

dado = input('Digite alguma coisa: ')

print(dado)
print(type(dado))
print('É número: {}'.format(dado.isnumeric()))
print('É decimal: {}'.format(dado.isdecimal()))
print('É título/Capitalizado: {}'.format(dado.istitle()))
print('É dígito: {}'.format(dado.isdigit()))
print('É espaço em branco: {}'.format(dado.isspace()))
print('É maiúsculo: {}'.format(dado.isupper()))
print('É minúsculo: {}'.format(dado.islower()))
print('É ASCII: {}'.format(dado.isascii()))
print('É alfa: {}'.format(dado.isalpha()))
print('É alfa-numérico: {}'.format(dado.isalnum()))
print('É identificador: {}'.format(dado.isidentifier()))
print('É imprimível: {}'.format(dado.isprintable()))