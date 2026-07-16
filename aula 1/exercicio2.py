nomeProduto = str(input("Digite o nome do produto: "));
precoProduto = float(input("Digite o preço do produto: "));
saldoEmConta = float(input("Digite o saldo em conta: "));

saldoRestante = precoProduto - saldoEmConta;

if saldoEmConta >= precoProduto:
    print("compra aprovada");
elif saldoEmConta < precoProduto:
    print("compra não aprovada, ainda faltam R$" + str(saldoRestante) + " para completar o valor do produto");



