# MÉDIA E SITUAÇÃO

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2) / 2
print(f'Sua média é {med:.2f}')
if med < 5:
    print('Você foi REPROVADO...')
elif 5 < med < 6.9:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você foi APROVADO!')
