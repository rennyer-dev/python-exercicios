# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = altura * largura
litros = area / 2

print('A parede mede {}m X {}m e sua área é {:.3f}m²'.format(largura, altura, area))
print('Para pintar essa parede completamente, serão necessários {:.4f}L de tinta'.format(litros))