L = [8, 21, 2, 9, 16, 12, 17, 19, 6, 10]

primeiro_impar = None
pos_primeiro_impar = -1

for i in range(len(L)):
    if L[i] % 2 == 1:
        primeiro_impar = L[i]
        pos_primeiro_impar = i
        break

if pos_primeiro_impar != -1:
    for i in range(pos_primeiro_impar, 0, -1):
        L[i] = L[i - 1]
    L[0] = primeiro_impar

print(L)
