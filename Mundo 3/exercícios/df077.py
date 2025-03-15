# EXERCÍCIO DE TUPLAS

palavras = ('Escrever', 'Desenhar', 'Grafitar', 'Programar',
            'Gato', 'Cachorro', 'Vaca', 'Coelho', 'Galinha',
            'Mesa', 'Porta', 'Janela', 'Telhado', 'Calha')
for frase in palavras:
    print(f'\nNa palavra {frase.upper()} temos: ', end='') # AQUI A FRASE À SER ANALISADA É LISTADA
    for vogais in frase: # AQUI, ELE ANALISA PARA VOGAIS, A PALAVRA NA CONTAGEM DA FRASE, COMO FRASE[1] -> ESCREVER
        if vogais.lower() in 'aeiou': # SE ESCREVER TIVER AEIOU, ELE FILTRARÁ
            print(vogais, end=' ') # E AQUI ELE FAZ O PRINT DAS VOGAIS

