# DESAFIO DE FORMATAÇÃO DE TEXTO

pessoa = str(input('Qual seu nome?: ').strip())
print(f'Nome maiúsculo: {pessoa.upper()}')
print(f'Nome minúsculo: {pessoa.lower()}')
print(f'Total de letras: {len(pessoa) - pessoa.count(' ')}')
print(f'Total de letras no 1° nome: {len(pessoa.split()[0])}')
