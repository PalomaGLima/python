L = [8, 21, 2, 9, 16, 12, 17, 19, 6, 10]

maior = L[0]
segundo_maior = L[0]
pos_maior = 0
pos_segundo_maior = 0

for i in range(len(L)):
    if L[i] > maior:
        segundo_maior = maior
        pos_segundo_maior = pos_maior
        maior = L[i]
        pos_maior = i
    elif L[i] > segundo_maior:
        segundo_maior = L[i]
        pos_segundo_maior = i


L[pos_maior], L[-1] = L[-1], L[pos_maior]

if pos_maior == len(L) - 1:
    pos_segundo_maior = len(L) - 2

L[pos_segundo_maior], L[-2] = L[-2], L[pos_segundo_maior]

print(L)
