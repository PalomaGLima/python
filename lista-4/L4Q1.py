L = [1, 8, 3, 12, 6, 15, 30, 19, 35, 36, 38]
cont = 0
N = len(L)

for i in range(len(L)-2):
    if (L[i] < L[i+2]):
        cont = 1

if (cont == 1):
    print('sim')
else:
    print('nao')
