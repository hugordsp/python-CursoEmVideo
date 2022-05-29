import os
os.system('cls')

confirma = 's'

while confirma == 's':

    distancia = float(input('Qual a distância do seu destino em Km? '))

    if distancia <=200:
        print(f'O valor cobrado pela sua viagem para um percruso de {"%.2f" % (distancia)} Km será de R${"%.2f" %(distancia * 0.5)}.')
        print()
    else:
        print(f'O valor cobrado pela sua viagem para um percruso de {"%.2f" % (distancia)} Km será de R${"%.2f" %(distancia * 0.45)}.')
        print()
    
    confirma = input('Deseja tentar novamente, digite s/n? ')
    while confirma != 's' and confirma != 'n':
        confirma = input('Deseja tentar novamente, digite s/n? ')
          
    print()  

print()
print('='*20, 'Fim do algoritmo', '='*20)
