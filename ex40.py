nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
média = (nota1 + nota2) / 2
if média >= 7:
    print("\033[0;32m Aprovado\033[m")
    print('Sua média foi {}'.format(média))
    print('Parabéns!!!')
elif média >= 5 or média <= 6.9:
    print("\033[0;33m Recuperação\033[m")
    print('Sua média foi {}'.format(média))
    print('Você é burro!!!')
else:
    print("\033[0;31m Reprovado\033[m")
    print('Sua média foi {}'.format(média))
    print('Você é burro!!!')
