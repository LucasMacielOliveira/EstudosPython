valores = [100, 250, 80, 300, 150]

acrescimo = [valor * 1.1 for valor in valores]

maioresIgual = [abacaxi for abacaxi in valores if abacaxi >= 150]

classificacoes = [
    "alto" if valor >= 150 else "baixo"
        for valor in valores
]

print(acrescimo)
print(maioresIgual)
print(classificacoes)


