import os
os.system('cls')

from random import choice

vetor=[]

for i in range(4):
    vetor.append(input(f'Digite o nome do {i+1}° aluno: '))

print()

print(f'O aluno escolhido para apagar o quadro foi {choice(vetor)}.')

print()

print('='*20, 'Fim do algoritmo', '='*20)
