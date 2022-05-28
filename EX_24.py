import os
os.system('cls')

nome = input('Digite o nome completo da pessoa: ').upper()

dividido = nome.split()

if dividido[0]=='SANTO':
    print('A palavra começa com "SANTO".')
else:
    print('A palavra não começa com "SANTO".')    
            
print()

print('='*20, 'Fim do algoritmo', '='*20)
