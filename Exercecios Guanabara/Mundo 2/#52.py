while True:
    sair = input('[S] Para finalizar o código: ')
    if sair == 's' or sair == 'S':
        break
    # Número de soma

    base = 0

    # Variaveis com informações

    num = int(input('Digite um número 🐱‍👓: '))

    # Estrutura

    for x in range(1, num+1):
        print(
              f'{x}', end = ' » ' )
        if num % x == 0:
            base += 1
            print(
                  f'{x}', end = ' ' )
    if base == 2:
        print(f'\n Número Primo')
    else:
        print('\n Número não é Primo')

