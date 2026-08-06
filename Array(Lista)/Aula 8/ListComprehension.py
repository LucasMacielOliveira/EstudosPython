# Ela é uma forma curta de criar listas usando um for.

# Forma tradicional 

quadrados = []

for numero in range(1,6):
    quadrados.append(numero ** 2)

print(quadrados)


# Usando List Comprehension

quadrados = [numero ** 2 for numero in range(1,6)]

print(quadrados)

#Achando numeros pares

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

# USANDO IF/ELSE

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = [
    "par" if numero % 2 == 0 else "impar"
    for numero in numeros
]

print(resultado)

