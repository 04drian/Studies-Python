# Programa que leia um valora em metro e converta em centimetro e milimetros

    # Recebimento das informações

numero_1 = float(input('Digite um número em metros: '))

    # Calculos

km = numero_1 / 1000
hct = numero_1 / 100
dct = numero_1 / 10
metros = numero_1 * 1
deci = numero_1 * 10
cent = numero_1 * 100
mili = numero_1 * 1000

    # Resultado

print(f'O número {numero_1} em: \n [KM] {km}\n [Hec] {hct}\n [Dec] {dct}\n [Met] {metros}\n [Deci] {deci}\n [Cent] {cent}\n [Mili] {mili}')