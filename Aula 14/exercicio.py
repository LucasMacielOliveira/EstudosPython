'''
Exercício de fixação

Crie uma classe Cliente com:

nome: getter e setter; não pode ficar vazio.
email: getter e setter; deve possuir @.
documento: somente leitura.
ativo: somente leitura.
Métodos ativar() e desativar().
Propriedade calculada situacao, retornando "Ativo" ou "Inativo".

'''

class Cliente:
    def __init__(self,nome, email, documento, ativo):
        self._nome = nome
        self._email = email
        self._documento = documento
        self._ativo = ativo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if not novo_email.strip() or "@" not in novo_email:
            raise ValueError("O email deve possuir '@' e não pode estar vazio.")
        self._email = novo_email

    @property
    def documento(self):
        return self._documento

    @property
    def ativo(self):
        return self._ativo

    def ativar(self):
        self._ativo = True

    def desativar(self):
        self._ativo = False

    @property
    def situacao(self):
        return "Ativo" if self._ativo else "Inativo"

cliente = Cliente(
    "Lucas",
    "lucas@email.com",
    "123.456.789-00",
    True
)

cliente.email = "novo@email.com"
cliente.ativar()

print(cliente.nome)
print(cliente.email)
print(cliente.documento)
print(cliente.situacao)