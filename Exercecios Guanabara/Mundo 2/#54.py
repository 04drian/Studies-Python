# Programa que leia o ano de nascimento de sete pessoas e mostre quantas são maiores de idade e quantas não atigiram, maioridade = 21 anos

    #import's

from datetime import datetime

    # Recebimento das informações

ano_atual = int(datetime.today().year)

cont = 0

    # Laço

for x in range(0, 7):
    ano_de_nascimento = int(input('Digite o ano em que você nasceu: '))

    idade = ano_atual - ano_de_nascimento

    if idade >= 21:
        
        cont += 1

menores = 7 - cont        

print(f'Das 7, {cont} são maiores de idade. {menores} Ainda são menores de idade.')