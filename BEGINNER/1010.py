produto1 = input().split(" ")
produto2 = input().split(" ")

cod1,qtd1,valor1 = produto1
cod2,qtd2,valor2 = produto2

total1 = (int(qtd1)) * (float(valor1))
total2 = (int(qtd2)) * (float(valor2))
totalAPagar = total1 + total2
print('VALOR A PAGAR: R$ %0.2f'%totalAPagar)