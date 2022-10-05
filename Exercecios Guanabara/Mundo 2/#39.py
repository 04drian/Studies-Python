# Import's

from datetime import date
import emoji

# Variáveis

text1 = emoji.emojize(
    
    f'Qual ano do seu nascimento?:cloud:: '
)

# Conta da idade atual

ano_nascimento = int(input(text1))
ano_atual = date.today().year
idade_atual = ano_atual - ano_nascimento

# idade mínima para o alistamento

idade_minima = 18

quanto_falta = idade_minima - idade_atual

ano_atrasado = ano_nascimento + idade_minima

# Iniciação de Verificação...

print(emoji.emojize
      (
       f'Quem nasceu no {ano_nascimento} tem {idade_atual} em {ano_atual}:snowman:'
       ))
# Atraso no alistamento
if idade_atual > idade_minima:
    print(emoji.emojize(
    
        f'Você deveria ter se alistado no ano de {ano_atrasado}!:balloon:'
    ))
# Tempo restante para se alistar
elif idade_atual < idade_minima:
    print(emoji.emojize(
    
        f'Você não tem idade o suficiente para se alistar no Exercito. \n'
        f'Falta {quanto_falta} anos para você se alistar :alarm_clock:'
    ))
# Idade = 18. Alistamente imediato
elif idade_atual == idade_minima:
    print(emoji.emojize(
    
        f'Você tem idade suficiente para se alistar e pode se alistar IMEDIATAMENTE !'
    ))

# Caso dê algum erro (Não é para dar...)
else:
    print(emoji.emojize(
        
        f'Informação inválida:mute:'
    ))