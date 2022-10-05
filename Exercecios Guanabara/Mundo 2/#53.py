
    
    # Variaveis
        #text_0 = 'Escreva uma palavra✍: '

# Recebimento das informações

palavra = str(input('Escreva uma palavra✍ : ')).strip().upper()

# Transformação

separada = palavra.split()

juntar = ''.join(separada)

inverter = ''

# Inversão 

for letra in range(len(juntar) - 1, -1, -1 ):
    inverter += juntar[letra]

# Apuração

if juntar == inverter:
    print(f'Você escreveu {juntar} e inverso {inverter}.')
    print('Essa palavra é um Palíndromo 💡')

else:
    print('Essa palavra não é um Palíndromo 🏮')
    