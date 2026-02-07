# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO"

cidade = input('Informe o nome da cidade: ').strip()
cidade_inicio = cidade[:5].lower()

print('"{}" começa com "santo" ? {}'.format(cidade, cidade_inicio == 'santo'))
