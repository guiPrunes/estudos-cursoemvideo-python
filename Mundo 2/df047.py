# CONTAGEM DE NÚMEROS PARES

from time import sleep
print('Programa de contagem de números pares')
c = int(input('Inicio: '))
d = int(input('Fim: '))
for cd in range(c, d+2, 2):
    print(cd)
    sleep(0.2)
print('Este é o fim...')