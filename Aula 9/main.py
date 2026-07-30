from calculos import aluguel
from calculos import calcularDesconto as desconto

try:
   valorDiaria =  float(input("Digite o valor da diaria: "))
   dias =  int(input("Digite a quantidade de dias: "))
   valorDesconto = float(input("Digite o valor do desconto: "))

   valorOriginal = aluguel(valorDiaria, dias)


   totalComDesconto = desconto(valorOriginal, valorDesconto)


   print(f"\nO valor original é: R$ {valorOriginal:.2f}")
   print(f"o valor com desconto é de: R$ {totalComDesconto}")


    
except ValueError:
   print("O usuário deve informar apenas números")





