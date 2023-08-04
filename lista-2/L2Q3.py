L = [4, 178, 17, 4, 1, 1, 14, 7, 4]

tem_consecutivos_iguais = False

for i in range(len(L) - 1):
    if L[i] == L[i + 1]:
        tem_consecutivos_iguais = True
        break

if tem_consecutivos_iguais:
    print("Sim, existem dois elementos consecutivos iguais na lista.")
else:
    print("Não, não existem dois elementos consecutivos iguais na lista.")