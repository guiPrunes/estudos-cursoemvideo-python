# EXERCÍCIO FUNÇÃO

def escreva(a):
    tam  = len(a) + 4
    print(f'{'~' * (tam)}')
    print(f'  {a}')
    print(f'{'~' * (tam)}')
 
a = str(input('Digite algo: ')).strip()
escreva(a)
