import os
os.system('cls')

numero = int(input('Digite um númerode 0 a 9999: '))

while numero<0 or numero>9999:
    numero = int(input('ERRO: Digite um númerode 0 a 9999: '))

dividido = str(numero)

dividido = ' '.join(dividido)

separado = dividido.split()

print(dividido)

print(separado)

print()

if len(separado)==1:
    print(f'unidade: {separado[0]}')
elif len(separado)==2: 
    print(f'unidade: {separado[1]}')
    print(f'dezena:  {separado[0]}')  
elif len(separado)==3:  
    print(f'unidade: {separado[2]}')
    print(f'dezena:  {separado[1]}')
    print(f'centena: {separado[0]}')
elif len(separado)==4:  
    print(f'unidade: {separado[3]}')
    print(f'dezena:  {separado[2]}')
    print(f'centena: {separado[1]}')
    print(f'milhar:  {separado[0]}')      
             
print()

print('='*20, 'Fim do algoritmo', '='*20)
