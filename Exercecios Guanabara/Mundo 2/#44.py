"""
- À vista dinheiro/cheque:
- 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

# Variaveis:

text_0 = 'Formas de pagamento 🎰'

text_1 = 'Preço dos produtos🧸:\n - R$ '

text_2 = 'Qual opção deseja ? 👀\n '

# Opções de pagamento:

dinheiro_cheque = '[1] À vista no dinheiro/cheque 🔮'

vista_cartao = '[2] À vista no cartão👤'

duas_x_cartao = '[3] 2x no cartão 👤'

tres_ou_mais_c = '[4] 3x ou mais vezes no cartão👤'

# Distinguindo opção selecionada/conta de desconto ou juros:

preco = float(input(text_1))

print(text_0)
# Conta de desconto

#desconto_1 = (preco * 10)/100 

#desconto_2 = preco - desconto_1

# Conta de desconto 2  (5%)
#desconto_5p = (preco * 5)/100

#desconto_5pp = preco - desconto_5p

# Distinguindo a opção:
print(f'{dinheiro_cheque}\n'
      f'{vista_cartao}\n'
      f'{duas_x_cartao}\n'
      f'{tres_ou_mais_c}')

opc = int(input(text_2))
if opc == 1:
      desconto_1 = (preco * 10)/100 

      desconto_2 = preco - desconto_1
      print(f'Você receberá 10% de desconto na sua compra.🧸\n'
            f'Ao total ficará {desconto_2}')
elif opc == 2:
      desconto_5p = (preco * 5)/100

      desconto_5pp = preco - desconto_5p
      print(f'Você receberá 5% de desconto na sua compra.🧸\n'
            f'Ao total ficará {desconto_5pp}')
elif opc == 3:
      parcela_2v = preco / 2
      print('Como você efetuou a compra em 2x no cartão.🧸\n'
            f'O preço ficará {parcela_2v} por mês.')
elif opc == 4:
      parcela = float(input(f'Quantas parcelas você deseja ?🧸\n'
                            f''))
      # Conta de Juros

      juros_1 = preco / parcela

      juros_2 = juros_1 + preco 
      print(f'Ao todo ficará R${juros_2} 🤖')                   
else:
      print('Informação inválida')