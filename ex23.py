p = int(input('Digite um número:'))
u = p // 1 % 10
d = p // 10 % 10
c = p // 100 % 10
m = p // 1000 % 10
print('Analisando o número {}'.format(p))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
