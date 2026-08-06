# O else é executado somente quando nenhum erro acontece dentro do try.
'''
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Você precisa digitar um número inteiro.")
else:
    print(f"O número digitado foi {numero}.")
'''
#entrada válida executa o else

# entrada inválida executa o except
'''
try:
    numeroUm = int(input("Digite o  primeiro número: "))
    numeroDois = int(input("Digite o segundo número: "))
    resultado = numeroUm / numeroDois

except ValueError:
    print("Digite apenas números inteiros")
except  ZeroDivisionError:
    print("A divisão não pode ser feita por zero")
else:
    print(f"o resultado é {resultado}")
finally:
    print(" Finalizando... ")
'''
# O raise permite que nós mesmos provoquemos uma exceção quando uma regra não for respeitada.

try:
    idade = int(input("Digite a idade: "))

    if idade < 0:
        raise ValueError("A idade não pode ser negativa")

except ValueError as error: 
    print(f"Erro: {error}")
else:
    print(f"A idade da pessoa é: {idade} anos de idade")
finally:
    print("encerrando programa...")
    