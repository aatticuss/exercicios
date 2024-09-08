def calcFatorial(number):
    fat = 1
    for i in range(1, number + 1):
        fat *= i
    return fat
num = int(input('Digite um número: '))
fat_result = calcFatorial(num)
print(f'O fatorial de {num} é: {fat_result}')
