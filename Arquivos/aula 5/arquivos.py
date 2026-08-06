#Arquivos em python

#jeito antigo de abrir um arquivo

arquivo = open("clientes", "w")

arquivo.write("Lucas")

arquivo.close()

#Jeito moderno

# w - ele escreve e subescreve
with open("clientes", "w") as arquivo:
    arquivo.write("Lucas")

# a - adiciona no final

with open("clientes", "a") as arquivo:
    arquivo.write("\nMaria")

# r - Apenas leitura

with open("clientes", "r") as arquivo:
    print(arquivo.read())
    



