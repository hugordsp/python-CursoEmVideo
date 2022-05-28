import os
os.system('cls')

nome = input('Digite o nome completo da pessoa: ')

print(f'O nome com todas as letras maiúsculas: {nome.upper()}')

print(f'O nome com todas as letras minúsculas: {nome.lower()}')

print(f'A quantidade de letras ao todo sem os espaços é: ', len(nome) - nome.count(' '))

dividido = nome.split()

print(f'A quantidade de letras do primeiro nome é {len(dividido[0])}.')

print()

print('='*20, 'Fim do algoritmo', '='*20)
