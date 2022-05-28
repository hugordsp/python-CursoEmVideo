import os
os.system('cls')

produto= float(input('Digite o valor do produto em reais: '))
desconto= float(input('Agora digite o valor do desconto que deseja dar ao produto: '))

print()

print(f'O produto obteu um desconto de R${produto-(produto*(1-(desconto/100)))} e seu valo final ficou em R${produto*(1-(desconto/100))}.')

print()

print('='*20, 'Fim do algoritmo', '='*20)
