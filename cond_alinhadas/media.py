nota1 = float(input('Qual foi sua nota no primeiro semestre? '))
nota2 = float(input('Qual foi sua nota no segundo semestre? '))
media = (nota1 + nota2) / 2
print(media)
if media <= 4:
    print('REPROVADO')
elif media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
