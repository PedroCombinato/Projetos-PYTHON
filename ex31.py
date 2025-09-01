d = int(input('Qual a distância da sua viagem em km? '))
if d <= 200:
    valor = d * 0.50
    print('O preço da viagem será R${:.2f}'.format(valor))
else:
    valor = d * 0.45
    print('O preço da viagem será R${:.2f}'.format(valor))