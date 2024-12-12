listaUm = [num for num in range(26)]
listaDois = [num for num in range(20) if num % 2 == 0]

def getUnion(list1, list2):
    unionList = []
    
    for j in range(len(list1)):
        unionList.append(list1[j])
        
    for i in range(len(list2)):
        if list2[i] in unionList:
            found = True
            break
        else:
            unionList.append(list2[i])
            
    return unionList

listaUniao = getUnion(listaUm, listaDois)

print(', '.join(map(str, listaUniao)))