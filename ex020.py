# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem sorteada.
import random

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('Sorteando a ordem...')
print(alunos)
