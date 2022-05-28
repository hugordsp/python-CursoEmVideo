import os
os.system('cls')

nome = input('Digite o nome completo da pessoa: ')

dividido = nome.split()

print(f'O primeiro nome da pessoa é: {dividido[0].title()}')

print(f'o último nome da pessoa é: {dividido[len(dividido)-1].title()}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
