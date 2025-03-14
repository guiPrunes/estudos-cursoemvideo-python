# CAIXA ELETRÔNICO

cinquenta = vinte = dez = um = 0 # variáveis contábeis

print(f'{' CAIXA ELETRÔNICO ':=^50}')
while True:
    valor = int(input('Digite o valor para saque: R$ '))
    print(f'{' EXTRATO DE CÉDULAS ':=^50}')
    while valor != 0:
        if valor >= 50:
            cinquenta = valor // 50
            valor -= cinquenta * 50
            print(f'CINQUENTA (R$ 50): {cinquenta}')
        if valor >= 20:
            vinte = valor // 20
            valor -= vinte * 20
            print(f'VINTE (R$ 20): {vinte}')
        if valor >= 10:
            dez = valor // 10
            valor -= dez * 10
            print(f'DEZ(R$ 10): {dez}')
        if valor >= 1:
            um = valor // 1
            valor -= um
            print(f'UM (R$ 1): {um}')
    continuar = str(input('Continuar sacando? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar sacando? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break




