# EXERCÍCIO DE TUPLAS

times = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo',
         'Athletico-PR', 'Bragantino', 'Palmeiras', 'Internacional',
         'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Juventude',
         'Grêmio', 'Vasco da Gama', 'Fluminense', 'Criciúma',
         'Corinthians', 'Atlético-GO', 'EC Vitória', 'Cuiabá')
print(f'Primeiros 5 colocados: {times[0:5]}')
print(f'Últimos 4 colocados: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times[::])}')
print(f'Grêmo: {times.index("Grêmio")}º colocado')