# Variáveis?

text1 = (
        
        f'Qual a sua primeira nota  ? '
    )
text2 = (
        
        f'Qual foi a sua segunda nota  ? '
)

# Informações?

nt1 = float(input(text1))

nt2 = float(input(text2))

# Verificação da nota:

md = 6

result = nt1 + nt2

result2 = result / 2

# Aprovado e Reprovado:

reprov = (
   
    f'Sua nota é de {result2:.2f} . Você foi REPROVADO ❌\n'
    f'ESTUDE MAIS DA PRÓXIMA'
)

aprov = (

    f'Sua note é de {result2:.2f} . Você foi APROVADO ✅\n'
    f'PARABÉNS'
)

extra = (

    f'Sua note é de {result2:.2f} . Você foi EXCELENTE NA PROVA ✅\n'
    f'PARABÉNS, CONTINUE ASSIM !'
)

# Apuração:

if result2 == md:
    print(aprov)
elif result2 > md:
    if result2 > md:
        print(extra)
elif result2 < md:
    print(reprov)
else:
    print('INVALIDO BROW')
