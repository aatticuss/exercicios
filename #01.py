num = []
pares = []
impares = []

print('insira os números: \nAperte 0 para encerrar')
while True:
    num = int(input(''))
    if (num == 0):
        print('Encerrando...')
        break
    elif num % 2 == 0:
        pares.append(num)
        print(f'O número {num} é par')
    else:
        impares.append(num)
        print(f'O número {num} é impar')

print(num)