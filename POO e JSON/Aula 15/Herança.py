'''
Herança

Herança permite criar uma classe nova aproveitando atributos e métodos de outra classe.

Pense assim:

Uma betoneira é um equipamento.
Um andaime é um equipamento.

Portanto, Betoneira e Andaime podem herdar de Equipamento.

'''

#Exemplo 

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

# 2. Criando uma classe filha

class Betoneira(Equipamento):
    pass


'''
A classe filha herdou:

O __init__;
A propriedade valor_diaria;
O método calcular_aluguel();
O método exibir_dados().

'''

# adicionando caracteristicas proprias

class Betoneira(Equipamento):
    def __init__(self, nome, valor_diaria, capacidade_litros):
        super().__init__(nome, valor_diaria)
        self.capacidade_litros = capacidade_litros


betoneira = Betoneira(
    "Betoneira profissional",
    120,
    400
)

print(betoneira.nome)
print(betoneira.capacidade_litros)
print(betoneira.calcular_aluguel(5))

'''

O super() representa a classe-pai:

super().__init__(nome, valor_diaria)

É como dizer:

“Execute o __init__ de Equipamento antes de continuar.”

'''