L = [17, 10, 6, 15, 9, 3, 42, 20, 16, 25, 5]

maior_sequencia = []
sequencia_atual = []

for i in range(len(L)):
    if L[i] % 2 == 1:  # Verifica se o número é ímpar
        sequencia_atual.append(L[i])
    else:
        if len(sequencia_atual) > len(maior_sequencia):
            maior_sequencia = sequencia_atual
        sequencia_atual = []

# Verifica a última sequência
if len(sequencia_atual) > len(maior_sequencia):
    maior_sequencia = sequencia_atual

if maior_sequencia:
    print(", ".join(map(str, maior_sequencia)))
else:
    print("A lista não contém números ímpares.")
