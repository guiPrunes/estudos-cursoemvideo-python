# EXECUTE DO DF108

import df108

n = float(input("Digite um número (R$): "))
print(f"O valor {df108.moeda(n)} + 10% é igual a {df108.moeda(df108.dezpercent(n))}.")
print(f"O valor de {df108.moeda(n)} - 10% é igual a {df108.moeda(df108.minusdezpercent(n))}.")
print(f"O dobro do valor de {df108.moeda(n)} é igual a {df108.moeda(df108.dobro(n))}.")
print(f"A metade do valor de {df108.moeda(n)} é igual a {df108.moeda(df108.metade(n))}.")