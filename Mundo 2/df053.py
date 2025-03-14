# IDENTIFICADOR DE PALÍNDROMOS

ask = str(input('Digite uma frase: ')).upper().strip()
words = ask.split()
together = ''.join(words)
cont = ''
for negative in range(len(together) - 1, -1, -1):
    cont += together[negative]
if cont == together:
    print(f'Você escreveu: {together}, seu inverso é: {cont}.')
    print('É um palíndromo.')
else:
    print(f'Você escreveu: {together}, seu inverso é: {cont}.')
    print('Não é um palíndromo.')

#criei uma frase, deixei em caps e tirei os espaços de fora.
#criei uma variavel de palavras, com o split separando elas
#criei uma variavel para juntar as palavras, ou tirando os espaços de dentro
#criei uma variavel vazia, para usar o for
#usa-se o for, com a quantidade de caractéres - 1, porque vai de 0 até a última e quero que comece de 1 até a última
#-1 até a última letra, -1 de trás pra frente
#variavel vazia recebe variavel vazia + a frase no inverso
# o resto tu sabe
