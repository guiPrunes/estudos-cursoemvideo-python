# TABUADA COM BREAK E FLAG C/ NÚMERO NEGATIVO

c = 1
while True:
    n = int(input('Qual valor de tabuada deseja ver?: '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} X {c} = {n*c}')
        c += 1
    c = 1
print('Tabuador encerrado!')