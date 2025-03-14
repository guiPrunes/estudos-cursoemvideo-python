# ANOS BISSEXTO

ano = int(input('Digite um ano qualquer: '))
cal = ano % 4
if cal == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} é NORMAL.')
