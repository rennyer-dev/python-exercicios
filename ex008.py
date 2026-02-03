# Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros.

medida = float(input('Informe a medida (m): '))
kilometros = medida / 1000
hectometro = medida / 100
decametro = medida / 10
decimetro = medida * 10
centimetros = medida * 100
milimetros = medida * 1000

print('Analisando {}m temos:'.format(medida))
print('{}Km'.format(kilometros))
print('{}hm'.format(hectometro))
print('{}dam'.format(decametro))
print('{:.0f}dm'.format(decimetro))
print('{:.0f}cm'.format(centimetros))
print('{:.0f}mm'.format(milimetros))