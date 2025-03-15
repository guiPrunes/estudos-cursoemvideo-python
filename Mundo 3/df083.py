# VALIDAÇÃO DE PARÊNTESES NUMA EXPRESSÃO NUMÉRICA

monte = []

expr = str(input('Digite uma expressão: '))
for c in expr:
    if c == "(":
        monte.append("(")
    elif c == ")": 
        if len(monte)> 0: # se a lista não estiver vázia, ele vai tirar o último elemento
            monte.pop()
        else: # se a lista estiver vázia, ele vai adicionar um elemento
            monte.append(')')
            print(monte)
            break
# para cada "(", ele adiciona
# no ")", se a lista já tiver um "(" ou ")", ele tira deixando no 0
# então se tiver mais parênteses abertos do que fechados, ele vai sobrar na lista, dando erro

if len(monte) == 0:
    print(f'Sua expressão está correta!')
else:
    print(f'Sua expressão está errada!')