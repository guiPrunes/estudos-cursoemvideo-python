# ANÁLISE DE TEXTO

frase = str(input('Digite uma frase:')).lower().strip()
print(f'Qntd. de "A": {frase.count('a')}')
print(f'"A" pela primeira vez: {frase.find('a')+1}')
print(f'"A" pela última vez: {frase.rfind('a')+1}')
