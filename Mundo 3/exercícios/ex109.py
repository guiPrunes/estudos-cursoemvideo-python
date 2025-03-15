# EXECUTE DO DF109

import df109

n = float(input("Digite um número (R$): "))
print(f"O valor {df109.moeda(n, True)} + 10% é igual a {df109.dezpercent(n, True)}.")
print(f"O valor de {df109.moeda(n, False)} - 10% é igual a {df109.minusdezpercent(n, False)}.")
print(f"O dobro do valor de {df109.moeda(n, True)} é igual a {df109.dobro(n, False)}.")
print(f"A metade do valor de {df109.moeda(n, False)} é igual a {df109.metade(n, True)}.")