primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('razão:'))
décimo = primeiro_termo + (10-1)* razão
for c in range(primeiro_termo,décimo+razão,razão):
    print('{}'.format(c),end=' ⮕')
