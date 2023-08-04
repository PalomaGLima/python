L = [8, 4, 1, 9, 17, 12, 26, 13, 7, 14]

primeiro_impar = float('inf') 
segundo_impar = float('inf')   

for numero in L:
    if numero % 2 != 0:
        if numero < primeiro_impar:
            segundo_impar = primeiro_impar
            primeiro_impar = numero
        elif numero < segundo_impar:
            segundo_impar = numero

if segundo_impar != float('inf'):
    print("O segundo menor número ímpar na lista é:", segundo_impar)
else:
    print("-1")