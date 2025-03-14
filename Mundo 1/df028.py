# MINI JOGO DA ADIVINHAÇÃO

from random import randint
from time import sleep

print('Pensando em um número de 0 a 5...')
sleep(3) # FAZ O PC DORMIR, OU SEJA, ESPERAR ALGUNS SEGUNDOS
num = randint(0, 5) # USA RANDINT PARA NÚMEROS INTEIROS E NÃO O RANDOM PADRÃO
ask = int(input('Adivinhe o número que pensei: '))
print("Verificando fatores...")
sleep(3)
if num == ask:
    print("Acertou miserávi! Caba é bão mesmo...")
else:
    print(f"Pensei no número {num}, não no {ask}. Caba ruim!")
