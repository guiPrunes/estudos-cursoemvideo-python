# JOGO DA ADIVINHAÇÃO APRIMORADO

from random import randint
from time import sleep

cont = 1
print('Selecionando um número de 1 a 10...')
num_computador = randint(1, 10)
sleep(2.5)
print('Pronto!')
sleep(2)
pergunta = int(input('Adivinhe este número: '))
while not pergunta == num_computador:
    print(f"""\33[35mQue pena! Você errou!
N° do Computador: {num_computador}.
Seu N°: {pergunta}.\33[m""")
    repetir = str(input('Quer tentar de novo? [S/N]: ')).upper().strip()[0]
    if repetir in 'Ss':
        num_computador = randint(1, 10)
        pergunta = int(input('Digite outro número: '))
        cont += 1
    if repetir in 'Nn':
        break
if pergunta == num_computador:
    print(f"""\33[32mParabéns! Você acertou!
N° do Computador: {num_computador}.
Seu N°: {pergunta}.
N° de tentativas: {cont}.\33[m""")
