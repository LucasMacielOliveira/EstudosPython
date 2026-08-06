
import json
import requests


try:
    with open("enderecos.json", "r", encoding="utf-8") as arquivo:
        enderecos = json.load(arquivo)
except FileNotFoundError:
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

cepDigitado = input("Digite o Cep: ")

try:
    novoEndereco = consultar_cep(cepDigitado)
except ValueError as erro:
    print(erro)

else:
    cepExiste = any (
        endereco["cep"] == novoEndereco["cep"]
        for endereco in enderecos
    )

    if cepExiste:
        print("Esse CEP ja existe: ")
    else:
        enderecos.append(novoEndereco)
        with open("enderecos.json", "w", encoding="utf-8") as arquivo:
                json.dump(
                    enderecos,
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )
                
    print("\nEndereços encontrados:")

    for endereco in enderecos: 
        print(endereco["cep"])
        print(endereco["logradouro"])
        print(endereco["localidade"])
        print(endereco["uf"])