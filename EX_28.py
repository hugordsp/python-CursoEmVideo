import os
os.system('cls')
import random

confirma = 's'

while confirma == 's':

    sorteio = random.randint(0, 5) #gera um número aleatório entre 1 e 5
    numero = int(input("Digite um número de 0 a 5 para advinhar o número escolhido pelo computador: "))

    print()

    if numero==sorteio:
        print(f'Parabéns o número gerado pelo computador é igual a {numero}.')
        print()
    else:
        print(f'Infelizmente você errou, o número gerado pelo computador foi {sorteio}.')
        print()
    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
          confirma = input('Deseja tentar novamente, digite s/n? ')
    print()      

print()
print('='*20, 'Fim do algoritmo', '='*20)
