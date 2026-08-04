# Encapsulamento significa controlar como os dados de um objeto são acessados e modificados.

# 1. Atributo com _

#Em Python, o _ indica que o atributo é de uso interno:

#self._quantidade_disponivel = quantidade

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property # Property é um decorador que transforma o método em um atributo de leitura.
    def nome(self):
        return self._nome

    @nome.setter # Setters são métodos que permitem modificar o valor de um atributo de forma controlada.
    def nome(self, novo_nome):
        if not novo_nome.strip():
            raise ValueError("O nome não pode estar vazio.")

    

        self._nome = novo_nome


pessoa = Pessoa("Lucas")

print(pessoa.nome)

pessoa.nome = "Lucas Maciel"

print(pessoa.nome)

#------------------------------------------------------------------------------------#


class ContaBancaria:
    def __init__(self, saldo_inical, titular):
        self._saldo = saldo_inical
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo
    @property
    def titular(self):

        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        if not novo_titular.strip():
            raise ValueError("O titular não pode estar vazio.")
        self._titular = novo_titular
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = novo_saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("o valor tem que ser maior que zero.")
        self._saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("o valor tem que ser maior que zero.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor


print("\nConta Bancária")
conta = ContaBancaria(1000, "Lucas Maciel")

print(f"Titular: {conta.titular}")
print(f"Saldo: {conta.saldo}")

deposito = float(input("Digite o valor do depósito: "))
conta.depositar(deposito)
print(f"Saldo após depósito: {conta.saldo}")

saque = float(input("Digite o valor do saque: "))
conta.sacar(saque)
print(f"Saldo após saque: {conta.saldo}")
