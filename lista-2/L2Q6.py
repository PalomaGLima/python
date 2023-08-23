L = [15, 2, 11, 19, 21, 12, 3, 9, 6, 4]


if len(L) < 3:
    print("A lista deve conter pelo menos três elementos.")
else:
    maior = L[0]
    segundo_maior = L[1]
    terceiro_maior = L[2]

    for numero in L[3:]:
        if numero > maior:
            terceiro_maior = segundo_maior
            segundo_maior = maior
            maior = numero
        elif numero > segundo_maior:
            terceiro_maior = segundo_maior
            segundo_maior = numero
        elif numero > terceiro_maior:
            terceiro_maior = numero

    print("O terceiro maior elemento da lista é:", terceiro_maior)
