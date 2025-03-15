# EXERCÍCIO DE LISTA

lista = []
cont = cont5 = 0
while True:
    lista.append(int(input('Digite um número: ')))
    ask = str(input('Quer continuar? [S/N] ')).upper().strip()
    cont += 1
    if 5 in lista:
        cont5 += 1
    while ask not in "SN":
        ask = str(input('Digite uma opção válida...[S/N] ')).upper().strip
        cont += 1
    if ask == "N":
        break
lista.sort(reverse=True)
print("=-=" * 30)
print(f'Há {cont} números digitados na lista...')
print(f'LISTA: {lista}')
if cont5 == 0:
    print(f'O valor 5 NÃO está na lista...')
if cont5 >= 1:
    print(f'O valor 5 está na lista...')