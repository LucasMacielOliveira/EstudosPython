class pagamentoPix:
    def pagamento(self, valor):
        print(f"Pagamento de R${valor} realizado via Pix.")

class pagamentoCartao:
    def __init__(self, numero_parcelas):
        self.numero_parcelas = numero_parcelas

    def pagamento(self, valor):
        print(
            f"Pagamento de R${valor} em {self.numero_parcelas} parcelas "
            "realizado com cartão de crédito."
        )

class pagamentoDinheiro:
    def pagamento(self, valor):
        print(f"Pagamento de R${valor} realizado em dinheiro.")


pagamentos = [
    pagamentoPix(),
    pagamentoCartao(3),
    pagamentoDinheiro()
]

for pagamento in pagamentos:
    pagamento.pagamento(600)



