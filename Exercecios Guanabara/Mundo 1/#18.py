# Programa que leia um angulo e mostre Seno, Coseno e Tangente

# Import's

from math import cos,tan,sin,radians

# Recebimento das informações

numero_1 = int(input('Digite o ângulo: '))

# Calculos

seno = sin(radians(numero_1))

coseno = cos(radians(numero_1))

tangente = tan(radians(numero_1))

# Resultado

print(
    
    f'- Resultados:\n'
    f'[Seno] {seno:.2f}\n'
    f'[Coseno] {coseno:.2f}\n'
    f'[Tangente] {tangente:.2f}\n'
)