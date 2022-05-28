import os
os.system('cls')

from random import shuffle

vetor=[]
confirmar = input('Deseja iniciar o programa? ')

while confirmar!="sim" and confirmar!="nao":
    confirmar = input('ERRO: Digite "sim" ou "nao" se deseja iniciar o programa? ')

while confirmar=="sim":

    n= int(input('Quantas pessoas vão participar das apresentações? '))

    for i in range(n):
        vetor.append(input(f'Digite o nome do {i+1}° aluno: '))

    print()

    shuffle(vetor)
    
    print('A ordem de apresentação é:') 

    for i, numero in enumerate (vetor): #enumerar os números da lista
        print(f'{i+1}° => {numero}')

    print()    

    confirmar = input('Digite "sim" ou "nao" se deseja reiniciar o programa? ')

    while confirmar!="sim" and confirmar!="nao":
        confirmar = input('ERRO: Digite "sim" ou "nao" se deseja reiniciar o programa? ')
    if confirmar=="nao":
        break    

print()

print('='*20, 'Fim do algoritmo', '='*20)
