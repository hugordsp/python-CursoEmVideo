import os
os.system('cls')

from math import sqrt

cat_o = float(input('Digite o valor do cateto oposto: '))
cat_a = float(input('Digite o valor do cateto adjacente: '))
hipotenusa= sqrt((cat_o**2) + (cat_a**2))

print(f'O valor da hipotenusa é : {"{:.2f}".format(hipotenusa)}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
