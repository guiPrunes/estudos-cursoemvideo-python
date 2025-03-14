# PROGRESSÃO ARITMÉTICA 2.0

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
primeirotermo = primeiro
amais = 10
total = 0
contador = 0
while amais != 0:
    total += amais
    while contador <= amais:
        print(F'{primeirotermo} -', end=' ')
        primeirotermo += razao
        contador += 1
    print('PAUSA')
    amais = int(input('Mostrar mais quantos termos?: '))
print(f'A progressão foi finalizada com {contador} termos apresentados.')