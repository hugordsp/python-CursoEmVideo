import os
os.system('cls')

frase = str(input('Digite uma frase: ')).upper().strip()

contagem1 = frase.count('A')

pos1 = frase.find('A') + 1

pos2 = frase.rfind('A') + 1

print(f'1- A letra "A" teve {contagem1} na frase;')

print(f'2- A primeira ocorrência do "A" foi na posição {pos1}')

print(f'2- A últma ocorrência do "A" foi na posição {pos2}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
