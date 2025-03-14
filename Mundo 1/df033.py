# MAIOR OU MENOS NÚMERO

print('Digite três números diferentes.')
num1 = int(input('1° número: '))
num2 = int(input('2° número: '))
num3 = int(input('3° número: '))
menor = num1
maior = num3
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num3 < num2 and num2 < num1:
    maior = num1
if num3 < num2 and num2 > num1:
    maior = num2
print(f'O menor número foi {menor}, e o maior foi {maior}.')