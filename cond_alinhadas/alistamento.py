age = int(input('Qual o ano do seu nascimento? '))
ano = 2024 - age
print(ano)
if ano > 18:
    print('Você é maior de idade, o limite de alistamento já passou')
elif ano == 18:
    print('Está na hora de se alistar, você tem 18 anos')
elif ano < 18:
    print('Ainda não está na hora de se alistar, você é menor de idade')    