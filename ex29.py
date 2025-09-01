carro = int(input('Qual a velocidade do carro:'))
if carro > 80:
    v = (carro - 80) * 7
    print('VOCÊ FOI MULTADO!\n a multa será de {:.2f} '.format(v))
else:
    print('Parabéns, você não ultrapassou o limite de 80km/h')