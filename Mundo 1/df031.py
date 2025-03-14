# ´REÇO DA PASSAGEM SOBRE DISTÂNCIA PERCORRIDA

dis =  int(input('Digite a distância da viajem: '))
if 200 < dis:
    taf = dis * 0.45
    print(f'O preço da passagem é de R$ {taf}.')
else:
    taf = dis * 0.5
    print(f'O preço da passagem é de R$ {taf}')
print('=' * 17)
print('   Boa viajem!')
print('='* 17)
