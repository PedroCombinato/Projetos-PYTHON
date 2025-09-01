from random import randint
from time import sleep

print('[0] Papel')
print('[1] Pedra')
print('[2] Tesoura')
escolha = int(input('faça sua escolha: '))
itens = ('Papel','Pedra','Tesoura')
computador = randint(0,2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*11)
print('Você jogou {}'.format(itens[escolha]))
print('Computador jogou {}'.format(itens[computador]))
print('-='*11)
if escolha == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('COMPUTADOR VENCEU')
    elif computador == 2:
        print('VOCÊ VENCEU')

elif escolha == 1:
    if computador == 0:
        print('VOCÊ VENCEU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR VENCEU')

elif escolha == 2:
    if computador == 0:
        print('COMPUTADOR VENCEU')
    elif computador == 1:
        print('VOCÊ VENCEU')
    elif computador == 2:
        print('EMPATE')
else:
    print('\033[31mJOGADA INVÁLIDA')
print('Quer jogar novamente? ')
n = int(input('''[0] SIM
[1] NÃO
'''))
print('-'*30)
if n == 0:
    for c in range(1,11):
        print('[0] Papel')
        print('[1] Pedra')
        print('[2] Tesoura')
        escolha = int(input('faça sua escolha: '))
        itens = ('Papel', 'Pedra', 'Tesoura')
        computador = randint(0, 2)
        sleep(1)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1)
        print('-=' * 11)
        print('Você jogou {}'.format(itens[escolha]))
        print('Computador jogou {}'.format(itens[computador]))
        print('-=' * 11)
        if escolha == 0:
            if computador == 0:
                print('EMPATE')
            elif computador == 1:
                print('COMPUTADOR VENCEU')
            elif computador == 2:
                print('VOCÊ VENCEU')

        elif escolha == 1:
            if computador == 0:
                print('VOCÊ VENCEU')
            elif computador == 1:
                print('EMPATE')
            elif computador == 2:
                print('COMPUTADOR VENCEU')

        elif escolha == 2:
            if computador == 0:
                print('COMPUTADOR VENCEU')
            elif computador == 1:
                print('VOCÊ VENCEU')
            elif computador == 2:
                print('EMPATE')
        else:
            print('\033[31mJOGADA INVÁLIDA')
        print('Quer jogar novamente? ')
        n = int(input('''[0] SIM \n[1] NÃO'''))
        print('-' * 30)
else:
    print('Até a próxima')


