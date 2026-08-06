class Equipamento:
    def __init__(self,nome, valor_diaria, quantidade_disponivel):
        self.nome = nome
        self.valor_diaria = valor_diaria
        self.quantidade_disponivel = quantidade_disponivel

    def calcular_aluguel(self, dias, quantidade):

        if dias <= 0 or quantidade <= 0: 
            raise ValueError("Os dias e quantidades devem ser maiores que zero!!!")

        diaria = self.valor_diaria * dias * quantidade

        return diaria

    def alugar(self, quantidade):

        if quantidade > self.quantidade_disponivel or quantidade <= 0:
            raise ValueError("quantidade indisponivel")

        self.quantidade_disponivel -= quantidade

    def devolver(self, quantidade):

        if quantidade <= 0:
            raise ValueError("quantidade invalida")

        self.quantidade_disponivel += quantidade

    def exibir_dados(self):
        return (
        f"Nome do equipamento: {self.nome}\n"
        f"Quantidade Disponivel: {self.quantidade_disponivel}\n"
        f"Valor da diaria: {self.valor_diaria}"
        )


betoneira = Equipamento("Betoneira", 100, 3)

print(betoneira.calcular_aluguel(5, 2))
# 1000

betoneira.alugar(2)
print(betoneira.quantidade_disponivel)
# 1

betoneira.devolver(1)
print(betoneira.quantidade_disponivel)
# 2