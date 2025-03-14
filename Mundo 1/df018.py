# SEN / COS / TAN DE UM ÂNGULO

import math

#os ângulos dessas funções tem que estar em radianos

n = float(input('Digite o ângulo:'))
m = math.radians(n)
sen = math.sin(m)
cos = math.cos(m)
tan = math.tan(m)
print(f'O seno deste ângulo é {sen}, o cosseno é {cos} e a tangente é {tan}')