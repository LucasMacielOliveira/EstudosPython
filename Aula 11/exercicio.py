import requests

enderecos = []

def consultar_cep(cep):
    cep = cep.replace("-", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("O CEP deve possuir exatamente 8 números.")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    
    if dados.get("erro"):
        raise ValueError("CEP não encontrado.")
    
    return dados

for contador in range(3):
    cep = input(f"Digite o {contador + 1}º CEP: ")

    try: 
        endereco = consultar_cep(cep)
    except ValueError as erro:
        print(f"Erro: {erro}")
    else:
        enderecos.append(endereco)

for endereco in enderecos: 
    print("\nEndereços encontrados:")
    print(endereco["logradouro"])
    print(endereco["bairro"])
    print(endereco["localidade"])
    print(endereco["uf"])


