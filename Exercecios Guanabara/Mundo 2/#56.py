# Desenvolva um programa que leia NOME, IDADE e GÊNERO de 4 PESSOAS no final mostre a média de idade destas pessoas, o nome do homem mais velho...
# Quantas mulheres tem menos de 20 anos

# Listagem

si = 0
sf = 0
dc = {}
lista = []

# Laço

for p in range(0, 4):

    nome = str(input('Digite seu nome: ')).strip().capitalize()

    idade = int(input('Digite sua Idade: '))

    genero = str(input('Digite seu Gênero: ')).strip().upper()

    si += idade

    if genero == 'M':
        lista.append(idade)
        dc[idade] = nome

    elif idade < 20:
        sf += 1
    lista.sort()

if lista == []:
    lista = [0]

print(f'- Média de Idades: {si/4}\n- Nome do homem mais velho: {dc[lista[len(lista)-1]]}\n- Mulheres com menos de 20 anos: {sf}')