# FUNÇÕES

def area():
    t = l * c
    print(f'A área de um terreno {l}x{c} é de {t:.1f}m²')

print(' CONTROLE DE TERRENO ')
print(f'-' * 21)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area()