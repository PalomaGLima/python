import math
L = []

for i in range(3):
    y = float(input('adicione os lados do triangulo:'))
    L.append(y)

S = (L[0] + L[1] + L[2])/2

print(S)

area = math.sqrt(S*(S-L[0])(S-L[1])(S-L[2]))

print(area)