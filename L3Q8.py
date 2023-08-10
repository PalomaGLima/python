L = [1, 5, 6, 8, 9, 13, 15, 18, 19, 20]

x = int(input("Digite o número x: "))
y = int(input("Digite o número y: "))

indice_x = -1

for i in range(len(L)):
    if L[i] == x:
        indice_x = i
        break

if indice_x != -1:
    L[indice_x] = y

    while indice_x > 0 and L[indice_x - 1] > y:
        L[indice_x], L[indice_x - 1] = L[indice_x - 1], L[indice_x]
        indice_x -= 1

print(L)
