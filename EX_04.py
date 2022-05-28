import os
os.system('cls')

n = input('Digite algo: ')

print(f'O tipo primitivo é {type(n)}.')
print(f'É numérico? {n.isnumeric()}')
print(f'Só tem espaços? {n.isspace()}')
print(f'Só tem letras? {n.isalpha()}')

print('='*20, 'Fim do algoritmo', '='*20)