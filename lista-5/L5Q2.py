L = [2,1,3,1,3,2,4,1,3,2,1,2]
k = 3
N = len(L)
i = 0
while (i < N):
    if (L[i] == k):
        pos1 = 1
        print(pos1)
        break
    i = i + 1
i = N - 1
while (i>= 0):
    if (L[i] == k):
        pos2 = i
        print(pos2)
        break
    i = i - 1