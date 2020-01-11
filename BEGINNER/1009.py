nome = input()
salario = float(input())
vendas  = float(input())
salario_total = ((vendas*15)/100) + salario
print('TOTAL = R$ %0.2f'%salario_total)