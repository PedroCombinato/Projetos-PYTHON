r1 = int(input('Digite um valor: '))
r2 = int(input('Digite outro valor: '))
r3 = int(input('Digite outro valor: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;32mEssas retas podem formar um triangulo')
else:
    print('\033[1;31mEssas retas nao podem formar um triangulo')






