import os
os.system('cls')

confirma = 's'

while confirma == 's':

    salario = float(input('Informe qual o valor em reais do seu salário: '))

    if salario > 1250:
        print(f'O salário de R${"%.2f" % salario} terá um aumento de 10% e irá para R${"%.2f" % (salario * 1.1)}.')
    elif salario <= 1250:
        print(f'O salário de R${"%.2f" % salario} terá um aumento de 15% e irá para R${"%.2f" % (salario * 1.15)}.')

    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
          
    print()  

print() 
print('='*20, 'Fim do algoritmo', '='*20)