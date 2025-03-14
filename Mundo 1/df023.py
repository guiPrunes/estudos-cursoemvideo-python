# UNIDADE, DEZENA, CENTENA E MILHAR DE UM NÚMERO

ask = int(input('Digite um número entre 0 e 9999:'))
u = ask // 1 % 10
d = ask // 10 % 10
c = ask // 100 % 10
m = ask // 1000 % 10
print(f"""Seu número tem:
Unidades: {u}
Dezenas: {d}
Centenas: {c}
Milhares: {m}""")

