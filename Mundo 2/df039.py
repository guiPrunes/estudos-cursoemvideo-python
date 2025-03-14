# ALISTAMENTO MILITAR

nasc = str(input('Qual sua data de nascimento?: ')).strip()
if len(nasc) == 10:
    ano = int(nasc[6:])
else:
    ano = int(nasc.split()[-1])
alis = 2024 - ano
if alis <= 18:
    print('Você terá de se alistar!')
    print(f'Faltam {18 - alis} anos para o seu alistamento, está chegando a hora...')
elif alis == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou da hora do seu alistamento...')
    print(f'Passaram-se {alis - 18} anos desde o ano do seu alistamento')
