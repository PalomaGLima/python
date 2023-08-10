L = [11, 9, 12, 14, 6, 15, 21, 1, 4, 2]

maior_impar = None
pos_maior_impar = -1

for i in range(len(L)):
    if L[i] % 2 == 1 and (maior_impar is None or L[i] > maior_impar):
        maior_impar = L[i]
        pos_maior_impar = i

if pos_maior_impar != -1:
    for i in range(pos_maior_impar, len(L) - 1):
        L[i] = L[i + 1]
    L[-1] = maior_impar

print(L)
