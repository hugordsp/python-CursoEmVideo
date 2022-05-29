import os
os.system('cls')

confirma = 's'

while confirma == 's':

    r1 = int(input('Informe o tamanho da primeira reta: '))
    r2 = int(input('Informe o tamanho da segunda reta: '))
    r3 = int(input('Informe o tamanho da terceira reta: '))

    if (r1+r2 > r3) and (r1+r3 > r2) and (r2 + r3 > r1):
        print('Com esses 3 valores é possível formar um triângulo.')
    else:
        print('Com esses 3 valores não é possível formar um triângulo.')    

    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
          
    print()  

print() 
print('='*20, 'Fim do algoritmo', '='*20)