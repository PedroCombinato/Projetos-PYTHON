valor = float(input('Qual o valor do produto: '))
print('[1] À vista em dinheiro/cheque?')
print('[2] À vista no cartão?')
print('[3] Em até 2x no cartão?')
print('[4] 3x ou mais no cartão?')
forma = int(input('\n\033[32mQual a forma de pagamento? '))
if forma == 1:
    preço = valor*0.10
    final = valor - preço
    print('Você recebeu 10% de desconto.')
    print('O valor final é {}'.format(final))
elif forma == 2:
    preço = valor*0.05
    final = valor - preço
    print('Você recebeu 5% de desconto.')
    print('O preço final é {}.'.format(final))
elif forma == 3:
    print('Você não recebeu desconto.')
    print('O valor final é {}.'.format(valor))
elif forma == 4:
    preço = valor*0.20
    final = valor - preço
    print('Você recebeu 20% de juros na sua compra.')
    print('O valor final é {}.'.format(final))

