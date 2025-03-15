# MÓDULOS ( JUNTO COM EX109 )

def moeda(n,  c = False):
    if c == True:
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