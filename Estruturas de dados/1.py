numberList = [num for num in range(1, 21) if num % 3 == 0]

def getIndex(numList, target):
    for i in range(len(numList)):
        if numList[i] == target:
            return i
    return False
    
while True:
    num = int(input('Insira um número a ser pesquisado na lista. Digite 0 para encerrar.'))

    if num != 0:
        numIndex = getIndex(numberList, num)

        if numIndex:
            print(f'O número {num} foi encontrado na posição {numIndex} da lista')
        else:
            print(f'O número {num} não está presente na lista.')
            
    else:
        print('Encerrando...')
        break