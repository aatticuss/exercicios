lista = []

def bubbleSort(list):
    tamanho = len(list)
    troca = False
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                troca = True
        if not troca:
            break  
    return list

print('Adicione um número à lista. Digite 0 para sair. \n')
while True:
    num = int(input())
    
    if num != 0:
        lista.append(num)
        print(f'Número {num} adicionado com sucesso.')
    else:
        print('Encerrando...')
        print('Lista original:')
        print(', '.join(map(str, lista)))
        
        sortedList = bubbleSort(lista)
        print('Lista ordenada')
        print(', '.join(map(str, sortedList)))