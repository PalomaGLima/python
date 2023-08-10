L = [17, 10, 42, 15, 9, 30, 6, 25, 16, 20]

maior = L[0]
segundo_maior = L[0]
indice_maior = 0
indice_segundo_maior = 0

for i in range(len(L)):
    if L[i] > maior:
        segundo_maior = maior
        indice_segundo_maior = indice_maior
        maior = L[i]
        indice_maior = i
    elif L[i] > segundo_maior:
        segundo_maior = L[i]
        indice_segundo_maior = i

menor = L[0]
segundo_menor = L[0]
indice_menor = 0
indice_segundo_menor = 0

for i in range(len(L)):
    if L[i] < menor:
        segundo_menor = menor
        indice_segundo_menor = indice_menor
        menor = L[i]
        indice_menor = i
    elif L[i] < segundo_menor:
        segundo_menor = L[i]
        indice_segundo_menor = i

L[indice_segundo_maior], L[indice_segundo_menor] = L[indice_segundo_menor], L[indice_segundo_maior]

print(L)

