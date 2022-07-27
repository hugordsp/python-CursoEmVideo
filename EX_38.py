import os
os.system('cls')

confirma ='yes'
while confirma =='yes':
    numero1 = ''
    numero2 = ''
    numero1= int(input('Digite um valor inteiro para o primeiro número: '))  
    numero2= int(input('Digite um valor inteiro para o segundo número: '))
    print('\n'*2)
    if numero1>numero2:
        print('O primeiro valor é maior!')
    elif numero2>numero1:
        print('O segundo valor é maior!')
    elif numero1==numero2:
        print("Não existe valor maior, os dois são iguais.") 
    print('\n'*2)    
    confirma = input('Deseja fazer uma nova verificação? ')
    while confirma!= 'yes' and confirma!= 'no':  
        confirma = input('Deseja fazer uma nova verificação? ')
    print('\n'*2)
print('\nFim do algoritmo.\n')