# MÓDULOS ( JUNTO COM EX110 )

def moeda(n,  c = True):
    if c == False:
        return f'R$ {n:.2f}'.replace(".", ",")
    else:
        return f"{n:.2f}"

def dezpercent(a, c = False):
    return moeda(a + (10/100 * a), c)


def minusdezpercent(b, c = False):
    return moeda(b - (10/100 * b), c)
        
def dobro(x, c = False):
    return moeda(x * 2, c)

def metade (y, c = False):
    return moeda(y / 2, c)

def resumo(n):
    print("=" * 50)
    print(f"{"RESUMO":^50}")
    print("=" * 50)
    print(f"Preço analisado:    {moeda(n, False):>30}")
    print(f"Dobro do preço:     {dobro(n):>30}")
    print(f"Metade do preço:    {metade(n):>30}")
    print(f"10% de aumento:     {dezpercent(n):>30}")
    print(f"10% de redução:     {minusdezpercent(n):>30}")
    print("=" * 50)