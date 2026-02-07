# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = input('Informe o seu nome completo: ').strip()
nome_lista = nome.split()
nome_sem_espacos = ''.join(nome_lista)

print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Ao todo seu nome tem {} letras.'.format(len(nome_sem_espacos)))
print('Seu primeiro nome: "{}" tem {} letras.'.format(nome_lista[0], len(nome_lista[0])))