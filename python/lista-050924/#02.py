import random

num = []
positivos = []
negativos = []
zero_counter = 0

for i in range(10):
    num.append(random.randint(-10, 10))
    if num[i] > 0:
        positivos.append(num[i])
    elif num[i] < 0:
        negativos.append(num[i])
    else:
        zero_counter += 1

print(f'Dos números impressos, {len(positivos)} são positivos, {len(negativos)} são negativos e {zero_counter} são zeros')
print(f'Lista de positivos: {positivos}') 
print(f'Lista de negativos: {negativos}')