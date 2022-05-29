import os
os.system('cls')

confirma = 's'

while confirma == 's':

    ano = int(input('Digite o ano para verificar se este é bissexto: '))

    if ano%4==0 and ano%100!=0: 
        print('É um ano bissexto!')
    elif ano%4==0 and ano%100==0 and ano%400==0:
        print('É um ano bissexto!')   
    else:
        print('Não é um ano bissexto')    
    
    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
          
    print()  

print()
print('='*20, 'Fim do algoritmo', '='*20)