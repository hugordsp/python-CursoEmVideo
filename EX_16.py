import os
os.system('cls')

import math

num= float(input('Digite um número real qualquer: '))

print()
#forma 1
print(f'A porção inteira do número é {"{:.0f}".format(num)}')

print()
#forma 2
print(f'A porção inteira do número é {math.floor(num)}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
