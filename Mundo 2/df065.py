# SOMA E MAIOR E MENOR DE NÚMEROS

soma = contador = 0
ask = 'S'
maior = menor = 0
while ask == 'S':
    num = int(input('Digite um valor: '))
    if contador == 0:
        maior = num
        menor = num
    else:
        if num < maior:
            menor = num
        if num > maior:
            maior = num
    soma += num
    contador += 1
    ask = str(input('Digitar mais valores [S/N]?: ')).strip().upper()[0]
print(f'A média de todos os valores é: {soma / contador:.2f}')
print(f'Foram digitados {contador} números no programa. ')
print(f'O maior número registrado foi {maior} e o menor foi {menor}.')


