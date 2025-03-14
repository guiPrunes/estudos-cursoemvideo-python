# PROGRESSÃO ARITMÉTICA

pritermo = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dectermo = pritermo + (10-1) * r
#dectermo = 1  pode ser usado com um contador
#no caso de while dectermo <= 10

pa = pritermo
print(f'PROGRESSÃO ARITMÉTICA: {pritermo}', end=' - ')
while pa != dectermo:
    pa += r
    print(pa, end='')
    print(' - ' if pa < dectermo else '.', end='')
