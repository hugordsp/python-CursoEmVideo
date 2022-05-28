import os
os.system('cls')

salario = float(input('Digite o salário atual do funcionário em reais: '))

print()

print(f'O salário atual de R${salario} foi reajustado em 15% para R${round(salario*1.15, 2)}')

print()

print('='*20, 'Fim do algoritmo', '='*20)
