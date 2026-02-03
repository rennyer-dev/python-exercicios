# Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre sua média.

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))
media = (n1 + n2) / 2

print('\nCom as notas {} e {}:'.format(n1, n2))
print('A média do aluno é {:.1f}'.format(media))