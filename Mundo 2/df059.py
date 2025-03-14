# CALCULADORA

from time import sleep

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('Abrindo menu...')
    sleep(1.25)
    print('[ 1 ] SOMA')
    sleep(0.8)
    print('[ 2 ] MULTIPLICAR')
    sleep(0.8)
    print('[ 3 ] MAIOR')
    sleep(0.8)
    print('[ 4 ] NOVOS NÚMEROS')
    sleep(0.8)
    print('[ 5 ] SAIR DO PROGRAMA')
    sleep(0.8)
    opcao = int(input('> '))
    if opcao == 1:
        soma = numero1 + numero2
        print(F'RESULTADO: {soma}')
    if opcao == 2:
        multiplicar = numero1 * numero2
        print(f'RESULTADO: {multiplicar}')
    if opcao == 3:
        if numero1 > numero2:
            maior = numero1
            menor = numero2
            print(F'RESULTADO: {maior} > {menor}')
        if numero2 > numero1:
            maior = numero2
            menor = numero1
            print(F'RESULTADO: {maior} > {menor}')
    if opcao == 4:
        numero1 = int(input('Digite um novo número: '))
        numero2 = int(input('Digite um outro número: '))
