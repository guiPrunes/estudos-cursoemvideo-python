# MAIORES E MENORES DE IDADE

maior = 0
menor = 1
for nascimento in range(0, 7):
    ask = int(input('Ano de Nascimento: '))
    idade = 2024 - ask
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')
