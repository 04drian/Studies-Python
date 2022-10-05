# Programa que transforma Graus celcius° em F°
    
    # Recebimento das informações

temperatura = float(input('Digite a temperatura em celcius: '))

    # Calculo

temperatura_f = temperatura * 1.8 + 32

    # Resultado

print(f'A temperatura em F: {temperatura_f} °')