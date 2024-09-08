def inverterPalavra(user_input):
    palavra_invertida = ""
    for letra in user_input:
        palavra_invertida = letra + palavra_invertida
    if palavra == palavra_invertida:
        print(f'A palavra {user_input} é um palíndromo')
    else:
        print(f'A palavra {user_input} não é um palíndromo', '\n', f'Como ela fica invertida: {palavra_invertida}')

palavra = input("Digite uma única palavra: ")
while " " in palavra:
    print("Por favor, digite apenas uma palavra.")
    palavra = input("Digite uma única palavra: ")

inverterPalavra(palavra)
