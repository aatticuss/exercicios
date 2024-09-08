def gerarTabuada(number):
    tabuada = {}
    for i in range(1, 11):
        tabuada[i] = (i * number)
    
    print(f'Tabuada do {number}')
    for i in range(1, 11):
        print(f'{i} x {number} = {tabuada[i]}')
    
num = int(input('Digite um número: '))
gerarTabuada(num)