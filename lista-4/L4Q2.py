L = [7, 1, 10, 42, 1, 1, 30, 1, 25, 16, 8, 1, 5]

distancia_maxima = 0
distancia_atual = 0

for i in range(len(L)):
    if L[i] == 1:
        distancia_atual = 0
    else:
        distancia_atual += 1
    if distancia_atual > distancia_maxima:
        distancia_maxima = distancia_atual

print(distancia_maxima)
