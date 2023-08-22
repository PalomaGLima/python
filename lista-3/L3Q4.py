L = [8, 21, 2, 9, 16, 12, 17, 19, 6, 10]
N = len(L)
maior = 0
posma = 0

for i in range(0, N, 2):
    if (L[i] > maior):
        maior = L[i]
        posma = i
print(maior)

if (N % 2 == 0):
    posim = N - 1

else:
    posim = N - 1
L[posma] = L[posim]
L[posim] = maior

print(L)
