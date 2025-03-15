def fatorial(a, show=False):
    """
    É utilizado para calcular o fatorial(!) de um número natural.
    a = número natural à ser calculado.
    show = (opcional) mostra ou não o processo de cálculo.
    return = valor do fatorial de a.
    """
    f = 1
    for c in range(a, 0, -1):
        if show:
            if c == 1:
                print(f"{c} =", end=" ")
            else:
                print(f"{c} X", end=" ")
        f *= c
    return f
    

print(fatorial(6, True))
help(fatorial)