def leiaInt(a=str(input('Digite um número: '))):
    while a.isnumeric() == False:
            print('\033[0;31mE R R O ! Digite um número válido.\033[m')
            a = str(input('Digite um número: '))
            a.isnumeric()
    if a.isnumeric():
        a = int(a)
    return print(f'Você acabou de digitar o número {a}.')

leiaInt()  
