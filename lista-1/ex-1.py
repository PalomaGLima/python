nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
media = (nota1 + nota2)/2

if (media >= 7):
    print('media =%.2f ==> Aprovado' % media)

elif(media >= 4):
    print('media =%.2f ==> Avf' % media)
    notavf = float(input('digite a nota da avf:'))
    mediavf = (notavf + media)/2
    if (mediavf >= 5):
        print('mediavf = %.2f ==> aprovado' % mediavf)
    else:
        print('mediavf = %.2f ==> reprovado' % mediavf)

else:
    print('media = %.2f ==> reprovado' % media)