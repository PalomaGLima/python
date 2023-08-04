L = [8, 2, 5, 11, 29, 13, 6, 16, 7, 10]

soma = 0
quantidade = len(L)

for numero in L:
    soma += numero

media = soma / quantidade

print("A média dos números na lista é:", media)