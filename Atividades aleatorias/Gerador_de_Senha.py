import random

# Letras

lower = 'abcdefghijklmnopqrstuvwxyz'

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numeros = '0123456789'

simbolos = '!@#$%¨&*()+-_^~;.,;[{]}'

all = lower + upper + numeros + simbolos

limite = 10

senha = ''.join(random.sample(all, limite))

print(senha)

# Pão