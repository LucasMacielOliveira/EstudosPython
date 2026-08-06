'''''
import requests

url = "https://viacep.com.br/ws/01001000/json/"


resposta = requests.get(url, timeout=10)

print(resposta.status_code)
print(resposta.json())
'''


import requests


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


try:
    cep_digitado = input("Digite o CEP: ")
    endereco = consultar_cep(cep_digitado)

except ValueError as erro:
    print(f"Erro: {erro}")

except requests.exceptions.Timeout:
    print("A consulta demorou demais.")

except requests.exceptions.ConnectionError:
    print("Não foi possível acessar a internet.")

except requests.exceptions.HTTPError as erro:
    print(f"Erro HTTP: {erro}")

except requests.exceptions.RequestException as erro:
    print(f"Erro na requisição: {erro}")

else:
    print("\nEndereço encontrado:")
    print(f"Logradouro: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['localidade']}")
    print(f"Estado: {endereco['uf']}")

finally:
    print("\nConsulta encerrada.")