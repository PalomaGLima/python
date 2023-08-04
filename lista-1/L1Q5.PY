L = []

pesoX = 2
pesoY = 1
for i in range(2):
    a = float(input('Insira uma número:'))
    L.append(a)
somaP = (L[0]*pesoX)+(L[1]*pesoY)
peso = pesoX+pesoY
mediaP = somaP/peso
print('A media ponderada dos números é: %.2f' % (mediaP))
