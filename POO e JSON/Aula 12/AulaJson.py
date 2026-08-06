''' 


import json

cliente = {
    "nome": "Lucas",
    "cidade": "São Paulo",
    "ativo": True
}

with open("cliente.json", "w", encoding="utf-8") as arquivo:
    json.dump(
        cliente,
        arquivo,
        ensure_ascii=False,
        indent=4
    )

try:
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)

except FileNotFoundError:
    clientes = []
    print("O arquivo ainda não existe.")

except json.JSONDecodeError:
    clientes = []
    print("O arquivo contém um JSON inválido.")

else:
    print("Dados carregados com sucesso.")

print(clientes)

# Carregando dados
with open("cliente.json", "r", encoding="utf-8") as arquivo:
    cliente = json.load(arquivo)

print(cliente)
print(cliente["nome"])

# Tratando arquivos inexistentes ou inválidos

try:
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)

except FileNotFoundError:
    clientes = []
    print("O arquivo ainda não existe.")

except json.JSONDecodeError:
    clientes = []
    print("O arquivo contém um JSON inválido.")

else:
    print("Dados carregados com sucesso.")

print(clientes)

# Funções reutilizáveis

def carregar_enderecos():
    try:
        with open("enderecos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("O arquivo está inválido.")
        return []


def salvar_enderecos(enderecos):
    with open("enderecos.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            enderecos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

enderecos = carregar_enderecos()

novo_endereco = {
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "cidade": "São Paulo",
    "uf": "SP"
}

enderecos.append(novo_endereco)
salvar_enderecos(enderecos)

print("Endereço salvo!")

#-----------------------------------------------------------#

'''
#json.dump(): Python para arquivo JSON.
#json.load(): arquivo JSON para Python.
#json.dumps(): Python para uma string JSON.
#json.loads(): string JSON para Python.

'''

'''