import random

lista_primos = []
numeros = []
for i in range(20):
    numeros.append(random.randint(1, 10))

for num in numeros:
    primo = True
    if (num < 2):
            primo = False
    for i in range(2, num):    
        if (num % i == 0):
            primo = False
            break
    if primo:
        lista_primos.append(num)
    
print(lista_primos)
