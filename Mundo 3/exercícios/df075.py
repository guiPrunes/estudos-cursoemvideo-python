# EXERCÍCIO DE TUPLAS 

cont = 0

numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),
          int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'VOCÊ DIGITOU OS NÚMEROS: {sorted(numeros)}')
if 9 in numeros:
    cont += 1
print(f'VEZES EM QUE (9) APARECEU: {cont}')
if not 3 in numeros:
    print('NÃO HÁ (3) NOS NÚMEROS DIGITADOS')
else:
    print(f'PRIMEIRO (3) DIGITADO: {numeros.index(3)}')
print('NÚMEROS PARES DIGITADOS: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')

