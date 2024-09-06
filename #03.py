numbers = []

print('insira os números: \nAperte 0 para encerrar')
while True:
    num = int(input(''))
    if (num == 0):
        print('Encerrando...')
        break
    numbers.append(num)
if len(numbers) > 0:
    media_num = sum(numbers) / len(numbers)
    print(media_num)
else:
    print('Insira algum valor para realizar o calculo')