# Import's 

from time import sleep

# Variáveis

text1 = \
    f'Digite um valor 🎰: '

text2 = \
    f'Digite outro valor 🎰: '

text3 = \
    f'Digite o último valor 🎰: '

# Colcando as Variáveis para receber informações:

lado_1 = int(input(text1))

lado_2 = int(input(text2))

lado_3 = int(input(text3))

# Distinguir Equilátero, Isósceles e Escaleno:

# Equilátero
if lado_1 == lado_2 == lado_3:
    print(
        f'Os segmentos acime podem formar um Equilátero 🚩')
    # Escaleno   
elif lado_1 != lado_2 != lado_3 != lado_1:
    print(
        f'Os segmentos acima podem forma um Escaleno 🚩')
    # Isósceles
else:
    print(
        f'Os segmentos acima podem forma um Isósceles 🚩')
