# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Qual é o seu nome ? ')
print('Muito prazer em te conhecer, {}!'.format(nome))
# .format() vai fazer uma interpolação na string
# e a ordem de argumentos que for enviada para format() vai respectivamente tomar o lugar das chaves na string {}