class Equipamento:
    def __init__(self, nome, valor_diaria):
        self.nome = nome
        self.valor_diaria = valor_diaria

    @property
    def valor_diaria(self):
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor da diária deve ser positivo.")

        self._valor_diaria = novo_valor

    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser positiva.")

        return self.valor_diaria * dias

    def exibir_dados(self):
        return (
            f"Equipamento: {self.nome}\n"
            f"Valor da diária: R$ {self.valor_diaria:.2f}"
        )


class Betoneira(Equipamento):
    def __init__(self, nome, valor_diaria, capacidade_litros):
        super().__init__(nome, valor_diaria)
        self.capacidade_litros = capacidade_litros

    def exibir_dados(self):
        dados_principais = super().exibir_dados()

        return (
            f"{dados_principais}\n"
            f"Capacidade: {self.capacidade_litros} litros"
        )

class Andaime(Equipamento):
    def __init__(self, nome, valor_diaria, altura):
        super().__init__(nome, valor_diaria)
        self.altura = altura

    def exibir_dados(self):
        dados_principais = super().exibir_dados()

        return (
            f"{dados_principais}\n"
            f"Altura: {self.altura} metros"
        )
    
    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias)



try:
    andaime = Andaime(
        "Andaime tubular",
        25,
        2.5
    )

    print(andaime.exibir_dados())
    print(f"Aluguel: R$ {andaime.calcular_aluguel(10):.2f}")

except ValueError as erro:
    print(f"Erro: {erro}")