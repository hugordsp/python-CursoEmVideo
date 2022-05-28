import os
os.system('cls')

n= float(input('Digite um número para saber sua tabuada: '))

print()

for i in range(11):
    
    print(f'{n} x {i} = {n*i}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
