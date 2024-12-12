numberList = []

def getPares(numList):
    pares = []
    for i in range(len(numList)):
        if numList[i] % 2 == 0:
            pares.append(numList[i])
    return pares

print('Adicione um número à lista. Digite 0 para sair. \n')
while True:
    num = int(input())
    
    if num != 0:
        numberList.append(num)
        print(f'{num} foi adicionado à lista. \n')
    else:
        print('Saindo...')
        paresList = getPares(numberList)
        
        print('Números pares encontrados na lista que você definiu:')
        print(', '.join(map(str, paresList)))
        break