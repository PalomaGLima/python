L = [8, 2, 5, 11, 29, 13, 6, 16, 7, 10]

soma = 0
quantidade = len(L)

for numero in L:
    soma += numero

media = soma / quantidade

contagem_maiores = 0

for numero in L:
    if numero > media:
        contagem_maiores += 1

print("A quantidade de elementos maiores do que a média é:", contagem_maiores)