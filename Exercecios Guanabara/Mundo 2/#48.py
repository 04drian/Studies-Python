soma = 0
for a in range(1, 501):
    if (a % 2) != 0 and (a % 3) == 0:
        soma += a
print(soma)
