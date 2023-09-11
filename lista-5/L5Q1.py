L = [2,7,8,10,13,17,19,21,26,30]
k = 18
i = 0
N = len(L)
while(i<N):
    if(L[i] > k)and (L[i] % 2 != 0):
        print(L[i])
        break
    i = i + 1