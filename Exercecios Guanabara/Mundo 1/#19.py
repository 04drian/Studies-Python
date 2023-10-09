# Program que leia 4 nomes e sorteie aleatoriamente e escolha 1 

# Import's

import random 

# Recebimento das informações

nome_1 = str(input('Digite o primeiro nome > '))
nome_2 = str(input('Digite o segundo nome > '))
nome_3 = str(input('Digite o terceiro nome > '))
nome_4 = str(input('Digite o quarto nome > '))

# Lista

lista = [nome_1,nome_2,nome_3,nome_4]

# Resultado

print(f'O nome sorteado foi: {random.choice(lista)}')