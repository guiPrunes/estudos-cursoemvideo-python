# VALIDADOR DE SEXO

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0] #[0] para pegar a primeira letra
if sexo == 'M' or 'F':
    if sexo == 'M':
        print('Seu sexo é masculino.')
    if sexo == 'F':
        print('Seu sexo é feminino.')
    else:
        while sexo not in 'MF':
            sexo = str(input('Digite novamente [M/F]: ')).upper().strip()[0]
print('Acabou')
