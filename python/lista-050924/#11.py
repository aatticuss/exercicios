def contarLetras(user_input):
    contador = {}
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for letra in alfabeto:  
        contador[letra] = 0
    for letra in user_input:
            contador[letra] += 1
    for letra, contagem in contador.items():
        if contagem > 0:                 
            print(f'{letra} apareceu {contagem} vez(es)')

frase = input('Digite uma frase: ')
contarLetras(frase.lower())
