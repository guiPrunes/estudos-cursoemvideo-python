# LEITURA DE NOME DE CIDADE QUE COMECE COM SANTO

nc = input('Informe o nome da sua cidade:')
nc.title().strip()
print(f'Sua cidade começa com "Santo"?: {nc[:5] == "Santo"}')
