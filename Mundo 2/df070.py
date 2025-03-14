# CAIXA DE MERCADO

soma = milmais = maior = menor = 0
nmaior = nmenor = ''
contador = 1
print(f'{' CAIXA DE MERCADO ':=^35}')
while True:
    nome = str(input('Nome: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    if contador == 1:
        maior = preco
        menor = preco
        nmenor = nome
        nmaior = nome
    if contador > 1:
        if preco > maior:
            maior = preco
            nmaior = nome
        if preco < maior:
            menor = preco
            nmenor = nome
    if preco > 1000:
        milmais = 1
    soma += preco
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    contador += 1
    print(f'{'':=^35}')
print(f'{'':=^35}')
print(f'O total gasto na compra é R$ {soma:.2f}')
print(f'Há {milmais} produtos que custam mais que R$ 1000,00!')
print(f'O produto: {nmaior} (R$ {maior:.2f}) foi o mais caro. \nE o produto : {nmenor} (R$ {menor:.2f}) foi o mais '
      f'barato.')
