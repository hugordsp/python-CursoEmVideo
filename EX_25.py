import os
os.system('cls')

nome = str(input('Digite o nome completo da pessoa: ')).capitalize()

if 'Silva' in nome:
    print('Tem Silva no nome digitado.')
else:
    print('Não tem Silva no nome digitado.')    
            
print()

print('='*20, 'Fim do algoritmo', '='*20)
