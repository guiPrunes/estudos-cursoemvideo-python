# MENOR E MAIOR NUMA LISTA

lista = []
maior = menor = 0
for contagem in range(0,5):
    lista.append(int(input('Quantidade: ')))
    print(f'POSIÇÃO: {contagem}')
    if contagem == 0:
        maior = menor = lista[contagem]
    if contagem > 1:
        if lista[contagem] > maior:
            maior = lista[contagem]
        if lista[contagem] < maior:
            menor = lista[contagem]
print(f'O maior número é {maior} e aparece na posição ', end='')
for posicao, valor in enumerate(lista):
    if valor == maior:
        print(f'{posicao}...', end='')
print()
print(f'O menor número é {menor} e aparece na posição ', end='')
for posicao, valor in enumerate(lista):
    if valor == menor:
        print(f'{posicao}...',end='')

        

