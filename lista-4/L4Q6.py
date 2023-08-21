L = [9, 3, 2, 12, 6, 15, 7, 18, 5, 11, 14]

tamanho_sequencia_atual = 0
tamanhos_sequencias = []

for i in range(len(L)):
    if L[i] % 2 == 1:  # Verifica se o número é ímpar
        tamanho_sequencia_atual += 1
    else:
        if tamanho_sequencia_atual > 0:
            tamanhos_sequencias.append(tamanho_sequencia_atual)
            tamanho_sequencia_atual = 0

if len(set(tamanhos_sequencias)) == 1:
    print("Sim")
else:
    print("Não")
