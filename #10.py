num_list = []

def calcSoma(numbers):
    pares = 0
    if not numbers:
        print('Insira numeros válidos: ')
    else:
        for i in range(len(numbers)):
            if i % 2 == 0:
                pares += numbers[i]
    return pares

print('Digite os numeros: \nAperte 0 para encerrar.')
while True:
    num = (float(input('')))
    if num == 0:
        print('Encerrando...')
        break
    num_list.append(num)

soma_result = calcSoma(num_list)
print(f'A soma dos indices pares da lista é: {soma_result}')