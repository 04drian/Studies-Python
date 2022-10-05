from time import sleep

# Variáveis 

text1 = (

  f'Digite o valor da Casa desejada: '
)
text2 = (

  f'Qual é o seu Salário?: '
)
text3 = (

  f'Quantos anos o financiamento: '
)

# Etapa das Imformações :D

casa = float(input(text1))
sleep(1.2)
salario = float(input(text2))
sleep(1.2)
financiamento = float(input(text3))

# Calculos :D

prestacao = casa / (financiamento * 12)
minimo = salario * 30 / 100 

# Introdução do If, elif, else
if prestacao <= minimo:
  print(
    
    f'Seu emprestimo foi aceito :D'
    )
else:
  print(
  
    f'Seu emprestimo foi negado :C'
    )