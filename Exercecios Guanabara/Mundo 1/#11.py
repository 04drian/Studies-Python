# Programa que leia largura e altura e verigique quanto de tinta precisará para pintar a parede considerando 1 litro de tinta pinta 2m²

    # Recebimento das informações

altura = float(input('Digite a altura da parede: '))

largura = float(input('Digite a largura da parade: '))

    # Calculos

juncao = altura * largura

litros_de_tinta = juncao / 2

    # Resultado

print(f'Você ira precisar de {litros_de_tinta:.1f}2m² de tinta')