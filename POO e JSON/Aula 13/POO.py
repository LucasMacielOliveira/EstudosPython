'''

Programação Orientada a Objetos

A classe funciona como um molde. O objeto é algo criado a partir desse molde.

Na OLS, por exemplo:

Cliente seria uma classe.
Lucas, João e Maria seriam objetos diferentes dessa classe.

'''

# 1 - Criando uma classe

'''''
class Cliente:
    def __init__(self, nome, documento, email):
        self.nome = nome
        self.documento = documento
        self.email = email

Cliente1 = Cliente(
    "Lucas Maciel",
    "47604165877",
    "lucasmacieldeoliveira.987@gmail.com"
    )

print(Cliente1.nome)
print(Cliente1.documento)
print(Cliente1.email)


2. Entendendo o self

O self representa o próprio objeto que está sendo utilizado.

 -> cliente1.nome

É o atributo nome pertencente ao objeto cliente1.

Podemos criar vários objetos independentes:

cliente1 = Cliente("Lucas", "111", "lucas@email.com")
cliente2 = Cliente("João", "222", "joao@email.com")

print(cliente1.nome)
print(cliente2.nome)

Cada objeto guarda seus próprios dados.

 
#3. Criando métodos - metodos que pertecem a uma classe

'''

class Cliente:
    def __init__(self, nome, documento, email):
        self.nome = nome
        self.documento = documento
        self.email = email

    def exibirDados(self):
        return (
            f"Nome: {self.nome}\n",
            f"Documento: {self.documento}\n",
            f"email: {self.email}"
        )

    def atualizarEmail(self, novoEmail):
        if "@" not in novoEmail:
            raise ValueError("Email invalido")

        self.email = novoEmail


try: 
    cliente1 = Cliente (
        "Lucas",
        "47604165877",
        "lucas@gmail.com"
    )

    cliente1.atualizarEmail("lucas123@gmail.com")

except ValueError as erro:
    print(f"Erro: {erro}")

else:
    print(cliente1.exibirDados())