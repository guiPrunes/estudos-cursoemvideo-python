# SOMA DE NÚMEROS

contador = 1
soma = 0
ns = int(input('Digite um valor: '))
while ns != 999:
    soma += ns
    contador += 1
    ns = int(input('Digite um valor[999 PARA SAIR]: '))
print(f'A soma dos valores digitados é: {soma}')
print(f'Você digitou {contador + 1} números no programa.')
