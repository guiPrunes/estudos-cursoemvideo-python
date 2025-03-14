# SALÁRIO COM AUMENTO

sal = float(input('Digite seu salário: '))
if sal >= 1250:
    aum = (10/100 * sal) + sal
    print(f'Seu salário com aumento de 10% é igual a R${aum:.2f}!')
else:
    aum = (15/100 * sal) + sal
    print(f'Seu salário com aumento de 15% é igual a R${aum:.2f}!')
print("""
Aproveite seu aumento!
""")
