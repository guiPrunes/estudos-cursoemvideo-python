# EMPRÉSTIMO BANCÁRIO

p1 = float(input('Qual o valor da casa que deseja comprar?: '))
p2 = float(input('Qual é seu salário atual?: '))
p3 = int(input('Em quantos anos você deseja pagar essa casa?: '))
prest = p1 / (p3 * 12)
print(f'O valor da prestação é: {prest:.2f}')
if prest > 30 / 100 * p2:
    print('O empréstimo foi\33[31m NEGADO\33[m!')
elif prest == 30 / 100 * p2:
    print('O empréstimo está em\033[33m ANÁLISE\033[m.')
else:
    print('O empréstimo está\33[0;32m APROVADO\33[m!')
print('Tenha um bom dia!')
