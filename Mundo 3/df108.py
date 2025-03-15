# MÓDULOS ( JUNTO COM EX108 )
def moeda(n):
    n = float(n)
    if float:
        return f'R$ {n:.2f}'.replace(".", ",")


def dezpercent(a):
    return a + (10/100 * a)

def minusdezpercent(b):
    return b - (10/100 * b)
        
def dobro(c):
    return c * 2

def metade (d):
    return d / 2
    
