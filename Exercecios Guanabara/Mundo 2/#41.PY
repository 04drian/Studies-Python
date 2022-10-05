# Import's

from datetime import date
from time import sleep

""" Divisões
mirim = 9, 10
petiz = 11, 12
infantil = 13, 14
juvenil = 15, 16
junior = 17, 18, 19
senior = 20
"""

# Informações primárias:

ano_de_nascimento = int(input(

    f'Em que ano você nasceu ? 🎊 '
))

# Calculos:

ano_atual = date.today().year

idade_atual = ano_atual - ano_de_nascimento
sleep(2)
print(
    f'O/A atleta possui {idade_atual} anos'
)
# Divisão de idade

if idade_atual == 9 or idade_atual == 10:
    print(
        f'Classificação : Mirim 🎠'
    )
elif idade_atual == 11 or idade_atual == 12:
    print(
        f'Classificação : Petiz 🎪'
    )
elif idade_atual == 13 or idade_atual == 14:
    print(
        f'Classificação : Infantil 🥼'
    )
elif idade_atual == 15 or idade_atual == 16:
    print(
        f'Classificação : Juvenil 🩲'
    )
elif idade_atual == 17 or idade_atual == 18 and idade_atual == 19:
    print(
        f'Classificação : Junior 🤳'
    )
elif idade_atual == 20 or idade_atual > 20:
    print(
        f'Classificação : Senior 🏊‍♀️'
    )
else:
    print('invalido')
