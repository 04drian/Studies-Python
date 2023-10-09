# Pragrama que leia 4 nomes e os embaralhe

# Imports
from random import shuffle

# Recebimento de informações

nome_1 = str(input('Digite um nome > '))
nome_2 = str(input('Digite outro nome > '))
nome_3 = str(input('Digite outro nome > '))
nome_4 = str(input('Digite outro nome > '))

# Lista / embaralhamento

lista = [nome_1, nome_2, nome_3, nome_4]
shuffle(lista)

# Resultado

print(f'Está é a nova ordem: {lista}')