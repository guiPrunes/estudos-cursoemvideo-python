# JOGO DO PAR OU IMPAR

from random import randint

venc = ''
scor = ''
cont = 0
while True:
    esc = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    if esc not in 'PI':
        break
    num = int(input('Escolha um número [1-10]: '))
    nc = randint(1, 10)
    s = num + nc
    if s % 2 == 0:  # par
        scor = 'PAR'
        venc = 'P'
    elif s % 2 == 1:  # impar
        scor = 'ÍMPAR'
        venc = 'I'
    if esc == venc:
        print('Você ganhou!')
        print(f'O computador jogou {nc}, você {num}, a soma é {s}, o número é {scor}.')
        cont += 1
    else:
        print('Você perdeu!')
        print(f'O computador jogou {nc}, você {num}, a soma é {s}, o número é {scor}.')
        print(f'Você venceu {cont} vezes!')
        break
