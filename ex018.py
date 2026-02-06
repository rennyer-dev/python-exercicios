# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
# cosseno e tangente desse ângulo
import math

angulo = float(input('Digite um angulo: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('Para o angulo {}° temos os seguintes valores:'.format(angulo))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))