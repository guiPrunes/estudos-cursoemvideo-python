# HIPOTENUSA DE UM TRIANGULO

import math

co = int(input('Digite o cateto oposto:'))
ca = int(input('Digite o cateto adjacente:'))
print(f'A hipotenusa deste triângulo retângulo é: {int(math.hypot(co, ca))}')
