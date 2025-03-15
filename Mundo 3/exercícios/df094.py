# EXERCÍCIO DE DICIONÁRIOS

grupo = []
p = {}
média = 0

while True:
    p['nome'] = str(input('Nome: ')).capitalize().strip()
    p['sexo'] = str(input('Sexo [M/F] ')).upper()[0].strip()
    p['idade'] = int(input('Idade: '))
    grupo.append(p.copy())
    seg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if seg == 'N':
        break
print('=-='*25)
print(f'O grupo tem {len(grupo)} pessoas.')
for c, v in enumerate(grupo):
    média += (grupo[c]['idade']) / len(grupo)
print(f'A média de idades é de {média} anos.')
print(f'As mulheres cadastradas foram: ', end=' ')
for c, v in enumerate(grupo):
    if grupo[c]['sexo'] == 'F':
        print(f'{grupo[c]["nome"]}', end=' ')
for c, v in enumerate(grupo):
    if grupo[c]['idade'] > média:
        print()
        print(f'nome = {grupo[c]["nome"]}; sexo = {grupo[c]["sexo"]}; idade = {grupo[c]["idade"]};')