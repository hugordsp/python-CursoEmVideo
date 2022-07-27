import os
os.system('cls')

confirma ='yes'
while confirma=='yes':
    numero = 0
    numero = int(input('Digite um número inteiro: '))
    print('Digite 1 para converter o número para binário:')
    print('Digite 2 para converter o número para octal:')
    print('Digite 3 para converter o número para hexadecimal:')
    escolha = int(input('Digite uma das opções acima: '))
    
    while escolha!=1 and escolha!=2 and escolha!=3:
        escolha = int(input('ERRO: Digite uma das opções acima: '))

    if escolha==1:
       tipo= bin(numero)
       print(f'O formato em binário de {numero} é {tipo}') 
    elif escolha ==2:
        tipo= oct(numero)
        print(f'O formato em octal de {numero} é {tipo}')
    elif escolha ==3:
        tipo= hex(numero)
        print(f'O formato em hexadecimal de {numero} é {tipo}')    

    confirma = input('Deseja fazer uma nova conversão? ')
    while confirma!= 'yes' and confirma!= 'no':  
        confirma = input('Deseja fazer uma nova conversão? ')

print('\nFim do algoritmo.\n')