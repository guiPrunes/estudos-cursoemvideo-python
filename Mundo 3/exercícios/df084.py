# CADASTRO DE PESSOAS

galera = []
pessoas = []
maior = menor = 0 
while True:
    pessoas.append(str(input(f'Nome: ')))
    pessoas.append(int(input(f'Peso: ')))
    if len(galera) == 0:
        menor = maior = pessoas[1] #AINDA NÃO SE TORNOU COMPOSTO
    else:
        if len(galera) >= 1:
            if pessoas[1] >= maior:
                maior = pessoas[1]
            if pessoas[1] <= menor:
                menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    continuar = str(input(f'Deseja continuar? [S/N] ')).upper().strip()[0]
    while not continuar in 'SN':
        continuar = str(input(f'Digite novamente...[S/N] '))
    if continuar == 'N':
        break
print(f'FORAM CADASTRADAS {len(galera)} pessoas.')
print(f'MAIOR PESO: {maior}kg | ', end='')
for i in galera:
    if i[1] == maior:
        print(f'{i[0]}')
print(f'MENOR PESO: {menor}kg | ', end='')
for i in galera:
    if i[1] == menor:
        print(f'{i[0]}')
        