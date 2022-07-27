import os
os.system('cls')

confirma ='yes'
while confirma=='yes':
    print('Empréstimo bancário para casa própria:\n')
    casa = float(input('Qual o valor do empréstimo para casa própria em reais? '))
    salario = float(input('Qual a renda do comprador em reais? '))
    tempo = int(input('Em quantos meses será o financiamento? '))
    prestacao = casa/tempo

    if prestacao >= salario*0.3:
        print('Empréstimo negado, o valor da prestação excede 30% o salário da solicitante ')
    else:
        print('\nEmpréstimo aprovado!\n')
        print(f'Valor emprestado: R${"%.2f" %casa}') 
        print(f'Total de meses a pagar: {tempo}')  
        print(f'Valor da prestação: R${"%.2f" %prestacao}') 

    confirma = input('Deseja fazer uma nova simulação de empréstimo? ')
    while confirma!= 'yes' and confirma!= 'no':  
        confirma = input('Deseja fazer uma nova simulação de empréstimo? ')

print('\nFim do algoritmo.\n')