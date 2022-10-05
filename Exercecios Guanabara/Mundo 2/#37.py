# Variaveis

text1 =  \
        f'Digite o número desejado✔: '

binario =  \
          f'[1] Binário'

octal =  \
        f'[2] Octal'

hexdecimal =  \
             f'[3] Hexadecimal'

alt =  \
      f'[X] Sair'

text2 = \
        f'Digite a opção que deseja converter 🐱‍: '

# Informações iniciais

while True:

    n = int(input(text1))

    # Escolhas

    print(
          f'-----' * 5)

    print(binario)

    print(octal)

    print(hexdecimal)

    print(alt)

    print(
          f'-----' * 5)

    # Informações 2

    perg = str(input(text2))
    if perg == 'x' or perg == 'X':
        break
    elif perg == '1' or perg == '2' or perg == '3':
        if perg == '1':
            rio = str(bin(n))
            print(
                  f'{rio[2:]}')
        elif perg == '2':
            cta = str(oct(n))
            print(
                  f'{cta[2:]}')
        elif perg == '3':
            exa = str(hex(n))
            print(
                  f'{exa[2:]}')
        else:
            print(
                  f'Opção inválida ಥ_ಥ')