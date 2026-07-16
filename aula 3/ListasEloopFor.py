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