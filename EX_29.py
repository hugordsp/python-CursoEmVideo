import os
os.system('cls')

velocidade = int(input('Qual a velocidade do carro ? '))

if velocidade > 80:
    multa= (velocidade -80)*7
    print(f'O veículo ultrapassou a velocidade de 80 Km/h!')
    print(f'O condutor deve pagar uma multa de R${multa},00.')
else:
    print('Veículo dentro do limite de velocidade permitido.')    


print()
print('='*20, 'Fim do algoritmo', '='*20)
