def notas(*notas, sit=False):
    estatistica = dict()
    estatistica['total'] = len(notas)
    s = 0
    for c, v in enumerate(notas):
        if c == 0:
            estatistica['maior'] = v
            estatistica['menor'] = v
        else:
            if v > estatistica['maior']:
                estatistica['maior'] = v
            if v < estatistica['menor']:
                estatistica['menor'] = v
    for v in notas:
        s += v
    estatistica['média'] = s / len(notas)
    if sit:
        if estatistica['média'] > 6:
            estatistica['situação'] = 'ACIMA DA MÉDIA'
        if estatistica['média'] > 7:
            estatistica['situação'] = 'MUITO ACIMA DA MÉDIA'
        elif estatistica['média'] < 6:
            estatistica['situação'] = 'ABAIXO DA MÉDIA'
        elif estatistica['média'] < 4:
            estatistica['situação'] = 'MUITO ABAIXO DA MÉDIA'
    print(estatistica)



notas(2, 4, 2, 3, 9, 8, sit=True)

