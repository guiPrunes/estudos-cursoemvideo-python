# EXERCÍCIO DE DICIONÁRIOS

dici = {}
aluno = str(input('Nome: '))
média = float(input('Média: '))
dici['nome'] = aluno
dici['média'] = média
if média >= 6:
    dici['situação'] = 'Aprovado'
else:
    dici['situação'] = 'Reprovado'
print(f'Seu nome é {dici["nome"]}')
print(f'Sua média é {dici["média"]}')
print(f'Sua situação final é: {dici["situação"]}')