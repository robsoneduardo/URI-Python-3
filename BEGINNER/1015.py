import math

p1 = input().split(' ')
p2 = input().split(' ')

x1,y1 = p1
x2,y2 = p2

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

x = float((x2 - x1))
y = float((y2 - y1))

distancia = float(math.sqrt(x**2 + y**2))
print('%0.4f'%distancia)