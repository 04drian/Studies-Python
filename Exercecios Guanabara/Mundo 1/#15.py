# Programa de aluguel de carro

    # Recebimento das informações

dias = int(input('Quantos dias ficou com o carro? '))

km = int(input("Quantos KM's rodados? "))

    # Calculos

aluguel = dias * 60 + km * 0.15

    # Resultado

print(f'- Você ficou {dias} dias com o carro.\n- Rodou {km} km\n- Ao total você deve pagar R${aluguel}')