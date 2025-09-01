import random
num = int(input('tente advinhar o numero de 1 a 5:'))
lista = [1, 2, 3, 4, 5]
aleatório = random.choice(lista)
print(aleatório)
if num == aleatório:
    print('Parabéns,você acertou!')
else:
    print('Você perdeu!')