def aluguel(valorDiaria, dias):

   aluguelTotal = valorDiaria * dias

   return aluguelTotal


def calcularDesconto(totalAluguel, desconto): 

    valorFinal = totalAluguel - (totalAluguel * desconto / 100)

    if desconto < 0 or desconto > 100:
        raise ValueError("O desconto não pode ser menor que 0 nem maior que 100")

    return valorFinal
