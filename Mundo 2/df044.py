# MINHA LOJA

print("=" * 8, "Lolja do Prunes", "=" * 8)
print('')
print("""[ 1 ] Farinha de Rosca: R$  4,99
[ 2 ] Água Sanitária:   R$  9,99
[ 3 ] Controle Remoto:  R$ 15,99
[ 4 ] Cutelo:           R$ 49,99""")
print('')
item = int(input('Escolha um item: '))
if item > 4:
    print('Não temos este item, estamos com pouco estoque...')
else:
    qntd = int(input('Quantas unidades?: '))
    print("=" * 33)
if item == 1:
    valor = 4.99 * qntd
    print(f'Valor: R${valor:.2f}')
elif item == 2:
    valor = 9.99 * qntd
    print(f'Valor: R${valor:.2f}')
elif item == 3:
    valor = 15.99 * qntd
    print(f'Valor: R${valor:.2f}')
else:
    valor = 49.99 * qntd
    print(f'Carrinho: R${valor:.2f}')
pgto = int(input(f"""Qual a forma de pagamento?
[ 1 ] À vista | Dinheiro/Cheque
[ 2 ] À vista | Cartão
[ 3 ] Cartão  | 2x de R$ {valor / 2:.2f}
[ 4 ] Cartão  | 3x até 6x (20% de juros) 
-> """))
print("=" * 33)
if pgto > 4:
    print('Escolha uma forma de pagamento válida.')
elif pgto == 1:
    total = valor - (valor * 10/100)
    print(f"""À vista | Dinheiro/PIX:
Total: R$ {total:.2f}""")
    print("=" * 33)
elif pgto == 2:
    total = valor - (valor * 5/100)
    print(f"""À vista | Cartão
Total: R$ {total:.2f}""")
    print("=" * 33)
elif pgto == 3:
    print(f"""Cartão | 2x
- 1a Parcela: R$ {valor/2:.2f};
- 2a Parcela: R$ {valor/2:.2f}
Total: R$ {valor}""")
    print("=" * 33)
else:
    t3x = (valor + (20 / 100 * valor))
    p3x = t3x / 3
    p4x = t3x / 4
    p5x = t3x / 5
    p6x = t3x / 6
    print(f"""Cartão | 3x ou mais
[ 1 ] 3x de R$ {p3x:.2f}
[ 2 ] 4x de R$ {p4x:.2f}
[ 3 ] 5x de R$ {p5x:.2f}
[ 4 ] 6x de R$ {p6x:.2f}""")
    pgc3 = int(input('-> '))
    print("=" * 33)
    if pgc3 == 1:
        print(f"""- 1a Parcela: R$ {p3x:.2f}
- 2a Parcela: R$ {p3x:.2f}
- 3a Parcela: R$ {p3x:.2f}
Total da compra: R$ {t3x:.2f}""")
        print("=" * 33)
    elif pgc3 == 2:
        print(f"""- 1a Parcela: R$ {p4x:.2f}
- 2a Parcela: R$ {p4x:.2f}
- 3a Parcela: R$ {p4x:.2f}
- 4a Parcela: R$ {p4x:.2f}
Total da compra: R$ {t3x:.2f}""")
        print("=" * 33)
    elif pgc3 == 3:
        print(f"""- 1a Parcela: R$ {p5x:.2f}
- 2a Parcela: R$ {p5x:.2f}
- 3a Parcela: R$ {p5x:.2f}
- 4a Parcela: R$ {p5x:.2f}
- 5a Parcela: R$ {p5x:.2f}
Total da compra: R$ {t3x:.2f}""")
        print("=" * 33)
    else:
        print(f"""- 1a Parcela: R$ {p6x:.2f}
- 2a Parcela: R$ {p6x:.2f}
- 3a Parcela: R$ {p6x:.2f}
- 4a Parcela: R$ {p6x:.2f}
- 5a Parcela: R$ {p6x:.2f}
- 6a Parcela: R$ {p6x:.2f}
Total da compra: R$ {t3x:.2f}""")
        print("=" * 33)
print('Até mais!')