def ficha(a=0, b=0):
    if len(a) == 0:
        a = '<desconhecido>'
    print(f"O jogador {a} fez {b} gol(s) no campeonato.")

nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)