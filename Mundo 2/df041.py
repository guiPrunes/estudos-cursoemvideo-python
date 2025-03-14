# MODALIDADE POR IDADE

from datetime import date
nasc = str(input('Qual a data do seu nascimento?: ')).strip()
if len(nasc) == 10:
    ano = int(nasc[6:])
else:
    ano = int(nasc.split()[-1])
idade = date.today().year - ano
print(f'O atleta tem {idade} anos de idade.')
if idade <= 9:
    print('Você está na categoria: MIRIM')
elif 9 < idade <= 14:
    print('Você está na categoria: INFANTIL')
elif 14 < idade <= 19:
    print('Você está na categoria: JUNIOR')
elif 19 < idade <= 20:
    print('Você está na categoria: SÊNIOR')
else:
    print('Você está na categoria: MASTER')
