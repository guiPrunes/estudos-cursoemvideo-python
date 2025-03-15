# EXERCÍCIO DE LISTA

lista = []
contador = 0
while True:
    valor = int(input('Digite um valor: '))
    if contador == 0:
        lista.append(valor)
        contador += 1
    #else:
    #    for contagem in range(0, len(lista)):
    #        if valor == lista[contagem]:
    #            print('Valor não adicionado.')
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor não adicionado.')
    parar = str(input('Quer continuar? [S/N] ')).upper()
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if parar == 'N':
        lista.sort()
        print(f'Você digitou os números: {lista}')
        break
