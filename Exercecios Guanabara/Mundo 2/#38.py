# Variáveis

text1 = f'[1] Digite o primeiro número: '

text2 = f'[2] Digite o segundo número: '

# Introdução das Informações

nm1 = int(input(text1))

nm2 = int(input(text2))

# Descobrir quem é maior
if nm1 >= nm2:
    print(

        f'O primeiro número é maior.'
    )
elif nm1 <= nm2:
    print(

        f'O segundo número é maior que o primeiro.'
    )
else:
    print(

        f'Número invalido'
    )