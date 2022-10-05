# Programa que leia as informações do texto

    # Recebimento de informações

info = input('Escreva algo:')

    # Apuração

print(type(info))

print('A palavra é Numero? ', info.isnumeric())

print('A palavra é Texto? ', info.isalpha())

print('A palavra é Texto e Numerico? ', info.isalnum())

print('A palavra é Todo em maiusculo? ', info.isupper())

print('A palavra o é Todo em minusculo? ', info.islower())