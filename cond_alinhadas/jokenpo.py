import random

jokenpo = input('Escolha um: Pedra, papel, tesoura: ').strip().lower()

lista = ['pedra', 'papel', 'tesoura']
sorteador = random.choice(lista)

print(f'O computador escolheu: {sorteador.capitalize()}')
if jokenpo == sorteador:
    print('Empate!')
elif (jokenpo == 'pedra' and sorteador == 'tesoura') or \
     (jokenpo == 'tesoura' and sorteador == 'papel') or \
     (jokenpo == 'papel' and sorteador == 'pedra'):
    print('Você ganhou!')
else:
    print('O computador ganhou!')
