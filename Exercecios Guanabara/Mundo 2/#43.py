"""
Tabela de peso:
xMenor que 18,5:	Magreza	Fadiga, stress, ansiedade
18,5 a 25	:Peso normal	Menor risco de doenças cardíacas e vasculares
25 a 30:	Sobrepeso	Fadiga, má circulação, varizes
30 a 35:	Obesidade grau I	Diabetes, angina, infarto, aterosclerose
35 a 40	Obesidade grau II:	Apneia do sono, falta de ar
Maior que 40:	Obesidade grau III	Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC
"""

# Import's

from time import sleep

# Variaveis

text_1 = \
         f'Qual seu peso atual (KG)👤? '

text_2 = \
         f'Qual sua altura atual (M)🕴? '   

# Variáveis que recem IMFORMAÇÕES

peso = float(input(text_1))

altura = float(input(text_2))

# Calculos:

imc = peso / (altura * altura)

if 18.5 <= imc < 18.5:
    print(
          f'- Você tem Magreza Fadiga, stress e ansiedade. 🧍‍♂️🧍‍♀️'  )
elif imc > 18.5 and imc < 25:
    print(
          f'- Você está no Peso ideal. ✨')
elif imc > 25 and imc < 30:
    print(
          f'- Você está com Sobrepeso, Má circulação e varizes.🧍‍♂️🧍‍♀️ ' )
elif imc > 30 and imc < 35:
        print(
              f'- Você está com Obesidade grau I, diabetes, Angina \n corre risco de Infarto e Aterosclerose. 📢'  )
elif imc > 30 and imc < 35:
    print(
              f'Obesidade II, Apeneia do sono e Falta de ar 📢'  )
else:
    print(
          f'Você tem obesidade III, Refluxo, Dificuldade em se mover e etc... 🎎'  )
print(f'{imc:.2f}')