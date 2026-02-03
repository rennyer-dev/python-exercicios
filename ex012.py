# Faça um altoritmo que leia o preço de um produto e mostre seu novo preço, com 5%
# de desconto

preco = float(input('Informe o preço do produto: R$'))
desconto = preco * 0.05
preco_final = preco - desconto

print('O antigo preço era R${:.2f}'.format(preco))
print('Mas na promoção com 5% de desconto ficou R${:.2f}'.format(preco_final))