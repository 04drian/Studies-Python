# Import's

from time import sleep

import math

from cores import stl

from cores import cdt

# Repetição

while True:
    # Delay para repetição

    sleep(3.5)

    # Introdução

    print(f'''
    \033[{stl["negrito"]};{cdt["verde"]}m

                      Pão 👻
    ▄▀▀▄─▄▀▄─█───▄▀▀▄─█──█─█───▄▀▄─█▀▄─▄▀▀▄─█▀▄─▄▀▄─
    █──▄─█▀█─█───█──▄─█──█─█───█▀█─█─█─█──█─██▀─█▀█─
    ─▀▀──▀─▀─▀▀▀──▀▀───▀▀──▀▀▀─▀─▀─▀▀───▀▀──▀─▀─▀─▀─
    \033[{stl["negrito"]};{cdt["vermelho"]}m

                    Versão 1

    ''')
 
    # Variaveis

    text0 = f'\033[{stl["negrito"]};{cdt["verde"]}m'\
        \
            f'[1] Adição ✨\n'\
            f'[2] Subtração ✨\n'\
            f'[3] Multiplicação ✨\n'\
            f'[4] Divisão ✨\n'\
            f'[5] Potênciação ✨\n'\
            f'[6] Raíz ✨\n'\
            f'[7] Para sair 🚨 '        

    # Introdução das informações

    print(text0)

    escolha = int(input('Digite aqui📄: '))

    # Escolha de operações: 
        # Sair 🚨 
    if escolha == 7:
        break

    # Adição
    elif escolha == 1:
        print(f'\033[{stl["negrito"]};{cdt["azul"]}m')

        n1 = int(input('Escreva um número: '))
        n2 = int(input('Escreva outro número: '))
        soma = n1 + n2 
        print(f'Aqui está o resultado: {soma} ')

    # Subtração

    elif escolha == 2:
        print(f'\033[{stl["negrito"]};{cdt["roxo"]}m')

        n1 = int(input('Escreva um número: '))
        n2 = int(input('Escreva outro número: '))
        subtracao = n1 - n2
        print(f'Aqui está o resultado da operação: {subtracao}')

    # Multiplicação

    elif escolha == 3:
        print(f'\033[{stl["negrito"]};{cdt["ciano"]}m')

        n1 = int(input('Escre um número: '))
        n2 = int(input('Escreva outro número: '))
        multiplicacao = n1 * n2
        print(f'Aqui está o resultado desta operação: {multiplicacao}')

    # Divisão

    elif escolha == 4:
        print(f'\033[{stl["negrito"]};{cdt["ciano"]}m')

        n1 = int(input('Escreva o número que deseja dividir: '))
        n2 = int(input('Escreva outro número para ser o dividendo: '))
        divisao = n1 / n2
        print(f'Aqui está o resultado desta operação: {divisao}')
    
    # Potenciação

    elif escolha == 5:
        print(f'\033[{stl["negrito"]};{cdt["ciano"]}m')

        n1 = int(input('Ecreva um número: '))
        n2 = int(input('Escreva outro número:'))
        potencia = n1 ** n2
        print(f'Aqui está o resultado desta operação: {potencia}')
    # Raíz
    elif escolha == 6:
            print(f'\033[{stl["negrito"]};{cdt["ciano"]}m')

            n1 = int(input('Ecreva um número: '))
            n2 = int(input('Escreva outro número:'))
            raiz = math.sqrt(n1)
            raiz2 = math.sqrt(n2)
            print(f'Aqui está o resultado: {raiz} e {raiz2}')
    else: 
        print(f'\033[{stl["negrito"]};{cdt["vermelho"]}m')
        print('Inválido')