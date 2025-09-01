d = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
v = (d * 60) + (km * 0.15)
print('O valor final é de {:.2f}'.format(v))
