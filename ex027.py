# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente
# ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input('Informe o nome completo: ').strip()
nome_sep = nome.split()

print('Primeiro = {}'.format(nome_sep[0]))
print('Último = {}'.format(nome_sep[len(nome_sep) - 1]))