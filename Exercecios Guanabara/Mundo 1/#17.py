# Programa que leia o comprimento do cateto opsto e do cateto adjacente de um
# triângulo retângulo.

# Import's

from math import hypot

# Recebimento das informações

numero_1 = float(input('Digite o Primeiro número do cateto: '))

numero_2 = float(input('Digite o Segundo número do cateco: '))

# Resultado

print(f'O valor da Hipotenusa é: {hypot(numero_1,numero_2):.3f}')