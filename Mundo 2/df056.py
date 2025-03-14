# ANALISADOR DE SEXOS E ETC

feminino = 0
masculino = 0
soma = 0
de_menor_feminino = 0
mais_velho = 0
nome_mais_velho = ''
for c in range(1, 5):
    print(f'=' * 20, f'{c}o DA LISTA', '=' * 20)
    nome = str(input('Nome: ')).capitalize().strip()
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    if sexo == 'F': #opcional
        feminino += 1
    elif sexo == 'M': #opcional
        masculino += 1
    else: #opcional
        print('Digite uma opção válida...')
    ano = int(input('Idade(em anos): '))
    if sexo == 'M' and c == 1:
        mais_velho = ano
        nome_mais_velho = nome
    if sexo == 'M' and ano > mais_velho:
        mais_velho = ano
        nome_mais_velho = nome
    if sexo == 'F' and ano < 20:
        de_menor_feminino += 1
    soma += ano
totmedia = soma / 4
print('=' * 54)
print(f'MÉDIA: A soma das idades do grupo é {soma}, e sua média é: {totmedia:.0f} anos.')
if masculino == 0:
    print('HOMENS: Não há homens na listagem.')
else:
    print(f'HOMENS: O homem mais velho tem {mais_velho} anos, e se chama: {nome_mais_velho}.')
if feminino == 0:
    print('MULHERES: Não há mulheres na listagem.')
elif de_menor_feminino == 1:
    print(f'MULHERES: Há {de_menor_feminino} mulher menor de 20 anos.')
else:
    print(f'MULHERES: Há {de_menor_feminino} mulheres menores de 20 anos')
