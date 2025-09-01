salário = float(input('Qual é seu salário:'))
if salário > 1250:
    aumento = salário * 10/100
    total = aumento + salário
    print('\033[4;33;40mSeu novo salário será de {:.2f}\033[m'.format(total))
else:
    aumento = salário * 15/100
    total = aumento + salário
    print('\033[4;33;40mSeu novo salário será de {:.2f}\033[m'.format(total))
