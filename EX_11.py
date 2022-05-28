import os
os.system('cls')

largura= float(input('Digite o valor da largura em metros da parede que deseja pintar: '))
altura= float(input('Agora digite o valor da altura em metros da parede que deseja pintar: '))
area= largura*altura
litro_tinta= area/2 
print()

print(f'Para pintar {area} m² de parede você precisará de {litro_tinta} litros de tinta.')

print()

print('='*20, 'Fim do algoritmo', '='*20)
