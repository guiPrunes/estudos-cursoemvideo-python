# SOMA DOS NÚMEROS PARES DIGITADOS

soma = 0
cont = 0
for ask in range(0,6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A SOMA DOS NÚMEROS PARES ACIMA É: {soma}.')
print(f'NÚMEROS PARES APARECEM {cont} VEZES.')