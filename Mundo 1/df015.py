# PREÇO DA VIAGEM E DISTÂNCIA

km = float(input('Quantos Km você percorreu com seu carro alugado?: '))
d = int(input('Por quantos dias o carro foi alugado?:'))
vd = 60 * d
vkm = 0.15 * km
print(f'O preço a pagar é: R$ {vd + vkm:.2f}')
