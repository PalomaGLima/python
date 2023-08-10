L = [17, 10, 42, 15, 9, 30, 6, 25, 16, 20]
maior = L[0]
pos = -1
N = len(L)

for i in range(N):
    if (L[i] > maior) and (L[i] % 2 != 0):
        maior = L[i]
        pos = i


if (pos != -1):
    aux = L[N-1]
    L[N-1] = maior
    L[pos] = aux

print (L)
