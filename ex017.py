# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

cat_op = float(input('Informe o comprimento do cateto oposto: '))
cat_ad = float(input('Informe o comprimento do cateto adjacente: '))

print('Com o cateto oposto: {} e o cateto adjacente: {} temos:'.format(cat_op, cat_ad))
print('Hipotenusa: {:.2f}'.format(hypot(cat_op, cat_ad)))


# Tentei fazer na mão com a formula padrão he he O_o
#hipotenusa = (pow(cat_op, 2) + pow(cat_ad, 2)) ** (1/2)
#print(hipotenusa)