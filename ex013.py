# Faça um altoritmo que leia o  salário de um funcionário e mostre seu novo salário
# com 15% de aumento.

salario = float(input('Informe o seu salário: R$'))
aumento = salario * 0.15
novo_salario = salario + aumento

print('Seu antigo salário era R${:.2f}'.format(salario))
print('Agora seu novo salário com um aumento de 15% é R${:.2f}'.format(novo_salario))