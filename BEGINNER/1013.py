numero = input().split(' ')

a,b,c = numero
a = int(a)
b = int(b)
c = int(c)

maior = (a+b+abs(a-b))/2

resultado = int((maior + c + abs(maior - c))/2)
print('%d eh o maior'%resultado)


