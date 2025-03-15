# TABULAÇÃO DE MÉDIA DE ALUNOS

from time import sleep
#
alunos = []
nomes = []
notas = []
#
while True:
    nomes.append(str(input(f'NOME: ')))
    notas.append(int(input(f'{'1ª NOTA: '}')))
    notas.append(int(input(f'{'2ª NOTA: '}')))
    nomes.append(notas[:])
    nomes.append((notas[0] + notas[1]) / 2)
    alunos.append(nomes[:])
    notas.clear(), nomes.clear()
#
    req = str(input(f'CONTINUAR? [S/N]: ')).strip().upper()[0]
    while req not in 'SN':
        req = str(input(f'INVÁLIDO...CONTINUAR? [S/N] ')).strip().upper()[0]
#
    if req == 'N':
        print(f'=-='*10)
        print(f'{'No.':<5} {'NOME':^15} {'MÉDIA':>5}')
        print('-'*30)
        for i in range(0, len(alunos)):
            print(f'{i:<5}', end='')
            print(f'{alunos[i][0]:^15}', end='')
            print(f'{alunos[i][2]:>5}')
        print('-=-'*10)
        ask = int(input('MOSTRAR NOTAS DE QUAL ALUNO? [-1 | ESCAPE] >> '))
        while ask != -1:
            for i in range(0, len(alunos)):
                if i == ask:
                    print(f'As notas de {alunos[i][0]} são {alunos[i][1]}')
            ask = int(input('MOSTRAR NOTAS DE QUAL ALUNO? [-1 | ESCAPE] >> '))
        break
print('='*30)
print(f'FINALIZANDO...')
sleep(0.9)
print(f'ATÉ MAIS!!!')
