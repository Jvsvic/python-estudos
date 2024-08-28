ano = int(input('Qual ano você nasceu? '))
idade = 2024 - ano
print(idade)

if idade <= 9:
    print('MIRIM')
elif 10 <= idade <= 14:
    print('INFANTIL')
elif 15 <= idade <= 19:
    print('JUNIOR')
elif idade > 20:
    print('SENIOR')
else:
    print('MASTER')
