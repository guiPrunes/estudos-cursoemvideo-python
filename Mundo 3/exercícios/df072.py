# EXERCÍCIO DE TUPLAS

extenso = 'Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte'
leitura = int(input('Digite um número: [0-20] '))
while True:
    if 0 > leitura or leitura > 20:
        leitura = int(input('Digite um número válido: [0-20] '))
    if 0 <= leitura <= 20:
        break
print(f'Número por extenso: {extenso[leitura]}')

# ou

# while True:
#   leitura = int(input('Digite um número: [0-20] '))
#   if 0 <= leitura <= 20:
#       break
#   print('Digite um número válido. ', end='')