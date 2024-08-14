valor = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário mensal? '))
qtd_anos = int(input('Em quantos anos você deseja pagar? '))
parcelas = qtd_anos * 12
parcela_mensal = valor / parcelas
print(f'Você vai pagar em {qtd_anos} anos.')
print(f'O valor da parcela mensal: R${parcela_mensal}')
if parcela_mensal > salario * 0.30:
    print('O valor da parcela mensal excedeu.')
else:
    print('A simulação é permitida pode assim, efetuar a compra.') 