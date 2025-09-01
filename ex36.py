valor = float(input('Qual o valor da casa?'))
salário = float(input('Qual o seu salário?'))
tempo = int(input('Quantos anos de financiamento?'))
conta = valor * 12 / tempo
if conta < salário * 30 / 100:
    print('O emprestimo foi aprovado!')
else:
    print('O emprestimo foi reprovado!')