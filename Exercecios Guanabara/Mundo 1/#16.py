# Programa leia um número real e mostre sua parte inteira

# Import's

import math

# Recebimento das informações

numero_1 = float(input('Digite um valor: '))

# Conversão 

truncado = math.trunc(numero_1)

# Resultado

print(f'O valor digita foi {numero_1} e a sua porção inteira é {truncado}')

# Outro metado

# print(f'O valor digita foi {numero_1} e a sua porção inteira é {numero_1:.0f}')
