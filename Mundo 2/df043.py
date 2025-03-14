# CÁLCULADORA DE IMC

peso = float(input('Quanto você pesa?(Kg ou g): '))
altura = float(input('Qual sua altura?(m ou cm): '))
if peso > 1000:
    peso = float(peso / 1000)
if altura > 100:
    altura = float(altura / 100)
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f'Você está abaixo do peso, de acordo com seu IMC ({imc:.2f}).')
elif 18.5 <= imc < 25:
    print(f'Você está no peso ideal, de acordo com seu IMC ({imc:.2f}).')
elif 25 <= imc < 30:
    print(f'Você está acima do peso, de acordo com seu IMC ({imc}).')
elif 30 <= imc < 40:
    print(f'Você está obeso, de acordo com seu IMC ({imc}).')
else:
    print(f'Você está em obesidade mórbida, de acordo com seu IMC ({imc}).')
