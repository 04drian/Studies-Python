print('====================\n'
      '  10 Termos da PA🧶 \n' 
      '====================')
# Variavei com informações

numero_0 = int(input('Digite o primeiro número da PA🎯: '))

numero_1 = int(input('Digite um número para pular(Ex: 2)🎣: '))

vezes = numero_0 + (11 - 1) * numero_1

for repeticao in range(numero_0, vezes, numero_1):
    print(f'{repeticao}', end= ' → → ')
    
print('Fim')