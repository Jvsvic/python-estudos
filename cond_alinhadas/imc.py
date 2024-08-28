peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt ** 2)
print(f'O seu IMC é {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do peso.')
elif imc <= 24.9:
    print('Peso ideal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade mórbida')