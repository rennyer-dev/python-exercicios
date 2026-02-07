# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "SILVA" no nome

nome = input('Informe um nome: ').strip()
tem_silva = 'SILVA' in nome.upper()

print('"{}" tem "silva" no nome ? {}'.format(nome, tem_silva))