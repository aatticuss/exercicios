def calcQuad(number_list):
    quadrados = []
    for numero in number_list:
        quadrados.append(numero * numero)
    return quadrados

num = []

for i in range(5):
    num.append(int(input(f'Digite o {i +1} número da lista:')))
quadrados_list = calcQuad(num)
print(f'Os números inserido foram: {num}')
print(f'O quadrado deles é: {quadrados_list}')