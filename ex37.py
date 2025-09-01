num = int(input('DIgite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário fica {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal fica {}'.format(num, oct(num)[2:]))
elif opção ==3:
    print('{} convertido para hexadecimal fica {}'.format(num, hex(num)[2:]))