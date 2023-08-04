L = [11, 5, 8, 18, 28, 3, 6, 14, 7, 20]

menor_impar = float('inf')

for numero in L:
    if numero % 2 != 0 and numero < menor_impar:
        menor_impar = numero

if menor_impar != float('inf'):
    print("O menor número ímpar na lista é:", menor_impar)
else:
    print("-1")