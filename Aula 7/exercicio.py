destino = input("Informe o destino: ")
hotel = input("informe o Hotel: ")


try:
    diasDiaria = int(input("Digite a quantidade de dias: "))
    valorDiaria = float(input("Digite o valor da diaria: "))

    if diasDiaria <= 0 or valorDiaria <= 0:
        raise ValueError("A quantidade de dias e o valor da diaria devem ser maior que zero!")

except ValueError as erro:
    print(f"Erro: {erro}")

else:
    totalViagem = diasDiaria * valorDiaria
    print("\n====== RESUMO ======")
    print(f" O destino é: {destino}")
    print(f" O Hotel é: {hotel}")
    print(f" Diarias: {valorDiaria}")
    print(f" o valor total da viagem é de R$ {totalViagem}")
finally:
    print("finalizando...")