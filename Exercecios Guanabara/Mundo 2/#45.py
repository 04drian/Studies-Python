from time import sleep
import random

# Repetição

while True:

    # Variaveis

    opcoes_1 = ' [1] Pedra 🧱\n [2] Papel 📄 \n [3] Tesoura ✌ \n [4] Sair 🚩'

    jogada_computador = random.randint(1, 3)
    sleep(1)

    print(opcoes_1)

    jogada_pessoa = int(input('Escolha um número🪀: '))

    # Distinguindo a jogada

    if jogada_pessoa == jogada_computador:
        print(f'Houve um EMPATE! 😱')

    # Jogada com PEDRA 🧱

    elif jogada_pessoa == 1 and jogada_computador == 2:
        print('- O Computador Ganhou!')
        sleep(1)
        print('- Você jogou PEDRA e o Computador jogou PAPEL ! 📄')
    
    elif jogada_pessoa == 1 and jogada_computador == 3:
        print('- Você GANHOU!')
        sleep(1)
        print('- Você jogou PEDRA e o Computador jogou Tesoura ! 🧱')

 # Jogada com PAPEL 📄

    elif jogada_pessoa == 2 and jogada_computador == 1:
        print('- Você GANHOU!')
        sleep(1)
        print('- Você jogou PAPEL e o Computador jogou PEDRA !📄'  )
    elif jogada_pessoa == 2 and jogada_computador == 3:
        print('- O Computador GANHOU!')
        sleep(1)
        print('- Você jogou PAPEL e o Computador jogou Tesoura ! ✌' )

    # Jogada com TESOURA ✌

    elif jogada_pessoa == 3 and jogada_computador == 1:
        print('- O Computador Ganhou!')
        sleep(1)
        print('- Você jogou TESOURA e o Computador jogou Pedra ! 🧱')
    elif jogada_pessoa == 3 and jogada_computador == 2:
        print('- Você GANHOU!') 
        sleep(1)
        print('- Você jogou TESOURA e o Computador jogou PAPEL! 📄')
    # Sair
    elif jogada_pessoa == 4:
        break
    # Erro
    else:
        print('ERRO')