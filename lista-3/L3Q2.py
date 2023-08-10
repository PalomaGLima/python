L = [17, 10, 42, 15, 9, 30, 6, 25, 16, 20]

menor = L[0]
maior = L[0]
pos_menor = 0
pos_maior = 0

for i in range(len(L)):
    if L[i] < menor:
        menor = L[i]
        pos_menor = i
    if L[i] > maior:
        maior = L[i]
        pos_maior = i

L[pos_menor], L[pos_maior] = L[pos_maior], L[pos_menor]

print(L)





