U = [17, 10, 42, 15, 30, 9, 6, 20, 16, 25]
V = [6, 20, 16, 25, 17, 10, 42, 15, 30, 9]

# Verificar se as listas têm o mesmo tamanho
if len(U) != len(V):
    print("Não")
else:
    tamanho = len(U)
    encontrado = False

    # Tentar cada índice como ponto de rotação
    for i in range(tamanho):
        nova_lista = U[i:] + U[:i]

        # Verificar se a nova lista é igual a V
        if nova_lista == V:
            encontrado = True
            break

    if encontrado:
        print("Sim")
    else:
        print("Não")
