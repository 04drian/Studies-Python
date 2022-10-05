# Programa que leia um número e mostre seu dobro triplo e raiz 

    # Recebimento das informações

numero_1 = float(input('Digite um número: '))

    # Caulculos

dobro = numero_1 * 2 

triplo = numero_1 * 3 

raiz = numero_1 ** 0.5

    # Resultado

print(f'- O dobro do número {numero_1} é {dobro}\n- O triplo do número {numero_1} é {triplo}\n- A raíz do número {numero_1} é {raiz:.2f}')