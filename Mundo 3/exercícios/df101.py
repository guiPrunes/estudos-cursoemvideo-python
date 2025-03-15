#ajuda interativa help(*o que quer pesquisar)
#ou print(*o que quer pesquisar.__doc__)

#def variavel(a=0) | opcional = (parametro=0)
#   """
#   docstring
#   """

#local -> dentro de uma def
#global -> dentro do programa principal
#local /= global | global(local)

def voto(a):
    global ano
    ano = 2024 - ano
    if ano < 16:
        r = "NEGADO."
    elif 16 <= ano < 18 or ano >= 65:
        r = "OPCIONAL."
    else:
        r = "OBRIGATÓRIO."
    print(f"COM {ano} ANOS, SEU VOTO É: ", end="")
    return r

ano = int(input('ANO DE NASCIMENTO: '))
print(voto(ano))