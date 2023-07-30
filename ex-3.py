L = [1,2,3,4,5]
maior = 0
maior2 = 0
N = len(L)

for i in range (N):
    if(maior < L[i]):
        maior = L[i]

for i in range (N):
    if(maior2 < L[i]) and (L[i] != maior):
        maior2 = L[i]

print("O maior número é:", maior)
print("O segundo maior número é:", maior2)