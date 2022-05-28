import os
os.system('cls')

km= float(input('Quantos quilômetros foram rodados com o carro? '))
dias= int(input('Quantos dias o carro foi alugado? '))
total= (dias*60) +(km*0.15)
#Formata para ter 2 casas decimais.
formatado= "{:.2f}".format(total) 

print()

print(f'O total a pagar pelo aluguel do carro é R${formatado}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
