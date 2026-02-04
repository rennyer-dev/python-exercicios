# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import randint

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido para limpar o quadro é {}'.format(alunos[randint(0, 3)]))