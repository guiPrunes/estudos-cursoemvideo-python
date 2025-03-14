# PROGRESSÃO ARITMÉTICA 3.0

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
primeirotermo = primeiro
mais = 9
contador = 0
while mais != 0:
    while contador <= mais:
        print(F'{primeirotermo} -', end=' ')
        primeirotermo += razao
        contador += 1
    print('PAUSA')
    opcao = int(input('Mostrar mais quantos termos?: '))
    mais += opcao
    if opcao == 0:
        break
print(f'A progressão foi finalizada com {contador} termos apresentados.')

