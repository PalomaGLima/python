L = [8, 21, 2, 9, 16, 12, 17, 19, 6, 10]

maior_impar = float('-inf')
pos_maior_impar = -1

# Encontra o maior elemento em posição ímpar e sua posição
for i in range(1, len(L), 2):
    if L[i] > maior_impar:
        maior_impar = L[i]
        pos_maior_impar = i

if pos_maior_impar != -1:
    # Move o maior elemento ímpar para a última posição ímpar
    ultimo_impar = len(L) - 1
    L[pos_maior_impar], L[ultimo_impar] = L[ultimo_impar], L[pos_maior_impar]

print(L)
# errada
