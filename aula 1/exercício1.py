'''
Primeiro exercício — Par ou ímpar

Crie um arquivo chamado exercicio_01.py.

O programa deve:

Pedir um número inteiro.
Calcular o resto da divisão por 2.
Informar se o número é par ou ímpar.
'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

valor_total = num1 + num2 


if valor_total % 2 == 0:
    print(f"O valor total {valor_total} é par.")
else:
    print(f"O valor total {valor_total} é ímpar.")