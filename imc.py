peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)
print('O seu IMC é : {:.2f}'.format(imc))
if imc <= 18.5:
    print('você está abaixo do peso ideal')
elif imc <= 25:
    print('Você está no seu peso ideal')
elif imc <= 30:
    print('Você está com sobre peso')
elif imc <= 40:
    print('você está obeso')
else:
    print('você tem obesidade morbida')