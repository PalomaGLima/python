L = []
maior = 0
maior2 = 0

for i in range(3):
    y = float(input('adicione nota:'))
    L.append(y)

if(L[0]>L[1]):
    maior = L[0]
    maio2 = L[1]
else:
    maior = L[1]
    maior2 = L[0]        

for i in range(3):
    if(maior < L[i]):
        maior2 = maior
        maior = L[i]
        
print(maior)
print(maior2)
media = (maior + maior2)/2

if(media >= 7):
    print('media =%.2f ==> aprovado'% (media))
    
elif(media >=4):
    print('media =%.2f ==> avf'% (media))
    notaavf=float(input('digite a nota da avf:'))
    mediaavf=(notaavf+media)/2
    if(mediaavf>=5):
        print('mediaavf =%.2f ==> aprovado'% (mediaavf))
    else:
        print('mediaavf =%.2f ==> reprovado'% (mediaavf))
else:
    print('media =%.2f ==> reprovado'% (media))