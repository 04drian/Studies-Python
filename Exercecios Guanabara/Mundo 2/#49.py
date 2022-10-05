
while True:
    # Variaveis

    text_0 = 'Digite algum número ⚙: '
    text_1 = '[S] Para sair 🧧: '

    # Variaveis para receber informações

    numero_0 = int(input(text_0))

    # Saída

    saida = input(text_1)

    # Tabuada

    for repeticao in range(11):
        print(f'{numero_0} X {repeticao} =  {numero_0 * repeticao}')
    
    # Fim da repetição
    
    if saida == 'S' or saida == 's':
        break