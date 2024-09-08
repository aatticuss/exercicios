def gerarProduto(number_list):
    produto = 1
    for num in number_list:
        produto *= num
    return produto

num = []

for i in range(7):
    num.append(int(input(f'Digite o {i + 1}º numero da lista: ')))

num_prod = gerarProduto(num)
print(f'O produto de todos os numeros da lista é: {num_prod}')