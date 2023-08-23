L = [11, 5, 8, 18, 28, 3, 6, 14, 7, 20]

for numero in L:
    if numero % 2 != 0:
        menor_impar = numero
        break

for numero in L:
    if numero % 2 != 0 and numero < menor_impar:
        menor_impar = numero

if menor_impar is not None:
    print("O menor número ímpar na lista é:", menor_impar)
else:
    print("-1")
