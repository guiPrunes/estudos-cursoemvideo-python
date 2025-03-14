# CONVERSÃO DE NÚMEROS

n1 = int(input('Digite um número inteiro: '))
ask = int(input("""Escolha qual conversão você deseja realizar:
      BINÁRIO: 1
      HEXADECIMAL: 2
      OCTAL: 3
-> """))
if ask == 1:
    print(f"""Segue o número digitado, convertido para BINÁRIO:
    {bin(n1)[2:]}""")
elif ask == 2:
    print(f"""Segue o número digitado, convertido para HEXADECIMAL:
    {hex(n1)[2:]}""")
elif ask == 3:
    print(f"""Segue o número digitado, convertido para OCTAL:
    {oct(n1)[2:]}""")
else:
    print('Digite um número de conversão VÁLIDO...')
