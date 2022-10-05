# Program que leia o peso de 5 pessoas e mostre o maior e menor peso lido

# Pesos

maior = 0
menor = 0

# Laço

for p in range(1, 6):
    peso = float(input(f'Digite peso da {p}ª: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior {maior}')
print(f'Menor {menor}')
