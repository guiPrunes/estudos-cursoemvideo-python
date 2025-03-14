# SOMA DE NÚMEROS C/ BREAK

s = 0
while True:
    n = int(input('Digite um número inteiro (S/999): '))
    if n == 999:
        break
    s += n
print(f'A soma é igual a {s}.')