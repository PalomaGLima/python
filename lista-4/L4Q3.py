U = [6, 2, 19, 5, 7, 8]
V = [10, 9, 4, 8, 7, 5, 19, 2, 6, 20, 5, 3]

N = len(U)
M = len(V)

achei = 0

for i in range(M):
    if (V[i] == U[0]):
        achei = 1
        break
if (achei == 0):
    print('a lista U nao esta contida em V')
    quit()

j = i

for k in range(1, N - 1, -1):
    j += 1
    if (j == M):
        print(' a lista U nao esta dentro da lista V')
        quit()
    if (V[j] != U[k]):
        print('A lista U não está dentro da lista V')
        quit()

print('sim, a lista U esta dentro da lista V')
