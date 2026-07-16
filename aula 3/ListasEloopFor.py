
# AS LISTAS PODEM GUARDAR VÁRIOS TIPOS DE DADOS, INCLUSIVE OUTRAS LISTAS

lista = [1,2,3,4,5]

print(lista)

# podemos criar uma lista vazia também e ir adicionando elementos a ela

emptyList = []

    
emptyList.append(1)
emptyList.append(2)
emptyList.append(3)

print(emptyList)

# Podemos descobrir a quantidade de elementos de uma lista com a função len()

print(len(emptyList))


# Loop de repetição for - Ele percorre cada elemento da lista, um por vez, e executa o bloco de código para cada elemento

cliente = ["João", "Maria", "José", "Ana"]

for nome in cliente: 
    print(nome)

# Dicionarios são estruturas de dados que armazenam pares de chave-valor. Eles permitem acessar os valores associados a uma chave específica.

aluguel = { 
    "cliente": "Lucas",
    "quantidade de equipamentos" : 3,
    "dias": 5,
    "valor Final": 150.00
}

aluguel["id"] = 25 # Adicionando um novo par chave-valor ao dicionário

print(aluguel["quantidade de equipamentos"]) # Acessando o valor associado à chave "quantidade de equipamentos"


print(aluguel["id"]) 
###################################################

alunos = []

aluno1 = {
    "nome": "Lucas",
    "idade": 22,
    "curso": "Engenharia de Software"
}

aluno2 = {
    "nome": "Guilherme",
    "idade": 21,
    "curso": "Engenharia civil"
}

alunos.append(aluno1)
alunos.append(aluno2)

print(alunos)

for aluno in alunos: 
    print(aluno["nome"])
    print(aluno["idade"])


