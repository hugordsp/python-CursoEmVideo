import os
os.system('cls')

from math import cos, sin, tan

angulo= int(input('Digite o valor do ângulo em graus para descobrir o seno, o cosseno e a tangente: '))

print()

print(f'O cosseno de {angulo}° é {round(cos(angulo), 2)}')

print()

print(f'O seno de {angulo}° é {round(sin(angulo), 2)}')

print()

print(f'A tangente de {angulo}° é {round(tan(angulo), 2)}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
