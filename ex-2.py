tecla1 = int(input('digite sua primeira tecla:'))
tecla2 = int(input('digite sua segunda tecla:'))
tecla3 = int(input('digite sua terceira tecla:'))

if(tecla1 > tecla2):
    maior = tecla1
    if(tecla3 > maior):
        maior = tecla3
        print('maior = %.2f ==> tecla3' % maior)
    else:
        print('maior = %.2f ==> tecla1' % maior)

else:
    maior = tecla2
    if(maior > tecla3):
        print('maior = %.2f ==> tecla2' % maior)
    else:
        maior = tecla3
        print('maior = %.2f ==> tecla3' % maior)