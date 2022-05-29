import os
os.system('cls')

confirma = 's'

while confirma == 's':

    vet = []
    for i in range(3):
        vet.append(float(input(f'Digite o número {i+1}: ')))
    print()
    print(f'O maior número é {"%.0f" % max(vet)}') 
    print(f'O menor número é {"%.0f" % min(vet)}') 
    print()
    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
          
    print()  

print() 
print('='*20, 'Fim do algoritmo', '='*20)