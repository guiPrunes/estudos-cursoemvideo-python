# SEQUENCIA DE FIBONACCI    

n = int(input('Digite um número inteiro: '))
t1 = 0
t2 = 1
contador = 3
print(f'{t1} - {t2}', end=' ')
while contador <= n:
    t3 = t1 + t2 # soma
    t1 = t2 # ele faz o t1 virar o t2
    t2 = t3 # faz o t2 virar o t3, e o t3 refaz a soma dai, pois t1 + t2
    print(f'- {t3}', end=' ')
    contador += 1
print('- Fim')