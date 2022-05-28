import os
os.system('cls')

celsius = float(input('Digite a temperatura em graus celsius para conversão em graus fahrenheit: '))

conversao= (celsius*9/5)+32

print()

print(f'A temperatura em graus fahrenheit é {conversao}°F')

print()

print('='*20, 'Fim do algoritmo', '='*20)
