# LADOS DE UM TRIANGULO

ret1 = float(input('\033[97m1° Segmento: \033[m'))
ret2 = float(input('\033[31m2° Segmento: \033[m'))
ret3 = float(input('\033[32m3° Segmento: \033[m'))
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print('Seus segmentos \033[1mPODEM FORMAR\033[m um triângulo.')
    if ret1 == ret2 == ret3:
        print('Seu triângulo é EQUILÁTERO!')
    elif ret1 == ret2 or ret1 == ret3 or ret2 == ret3:
        print('Seu triângulo é ISÓCELES!')
    else:
        print('Seu triângulo é ESCALENO!')
else:
    print('Seus segmentos \033[1mNÃO PODEM FORMAR\033[m um triângulo.')

