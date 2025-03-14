# CADASTRO DE PESSOAS E VALIDAÇÃO DE IDADE

dmaior = homem = mdmenor = 0
sexo = continuar = ''
while True:
    print(f'{' CADASTRE UMA PESSOA ':=^35}')
    idade = int(input('Idade: '))
    if idade > 18:
        dmaior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mdmenor += 1
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{'':=^35}')
print(f'Há {dmaior} pessoas maiores de 18 anos cadastradas')
print(f'Foram cadastrados {homem} homens no programa.')
print(f'Há {mdmenor} mulheres menores de 20 anos cadastradas.')
