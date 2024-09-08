import random

def encontrarMaiores(number_list):
    maiores = []
    number_list.sort(reverse=True)
    for num in number_list:
        if len(maiores) < 2 and num not in maiores:
                maiores.append(num)
    return maiores

def encontrarMenores(number_list):
    menores = []
    number_list.sort()
    for num in number_list:
        if len(menores) < 2 and num not in menores:
            menores.append(num)
    return menores

num = []
for i in range(20):
    num.append(random.randint(0, 10))

menores = encontrarMenores(num)
maiores = encontrarMaiores(num)
print(num)
print(f'Os dois maiores números encontrados foram: {maiores} e os dois menores foram: {menores}')