# LIMITE DE VELOCIDADE NUMA RODOVIA

from time import sleep


print("-=-"*20)
print('Você está na estrada, com limite de velocidade de 80Km/h.')
print("-=-"*20)
vlc = int(input('A quantos Km/h você está digirindo nesse momento?: '))
mlt = (vlc-80)*7
if vlc <= 80:
    print("""Você está dentro do limite de velocidade. Não haverá multas para o senhor.""")
    print(' '*5, 'Boa viajem!')
else:
    print("""Você está fora do limite de velocidade, o senhor será multado...""")
    print("Calculando a multa...")
    sleep(4)
    print('='*20)
    print(f"Valor da multa é: R${mlt}")

