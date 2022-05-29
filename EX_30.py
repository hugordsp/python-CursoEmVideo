import os
os.system('cls')

confirma = 's'

while confirma == 's':

    numero = int(input('Digite um número inteiro qualquer: '))
    print()
    if numero%2==0:
        print('Esse número é par.')
        print()
    else:
        print('Esse número é impar')
        print()  

    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
    print()  

print()
print('='*20, 'Fim do algoritmo', '='*20)
