# ============================================================
# ABSTRAÇÃO - PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
# ============================================================
#
# Abstração é o princípio de definir O QUE um objeto deve fazer,
# sem precisar definir todos os detalhes de COMO ele fará aquilo.
#
# A ideia é mostrar apenas os comportamentos importantes e deixar
# os detalhes específicos para as classes responsáveis.
#
# Em Python podemos utilizar:
#
# ABC -> transforma uma classe em uma classe base abstrata.
#
# @abstractmethod -> define um método que as classes filhas são
# obrigadas a implementar antes de poderem ser instanciadas.
#
# Exemplo:
#
# from abc import ABC, abstractmethod
#
# class FormaPagamento(ABC):
#
#     @abstractmethod
#     def processar(self, valor):
#         pass
#
# Nesse caso, FormaPagamento define que TODA forma de pagamento
# deve possuir o método processar(), mas não determina exatamente
# como o pagamento será processado.
#
# As classes filhas definem COMO:
#
# class PagamentoPix(FormaPagamento):
#
#     def processar(self, valor):
#         return f"Pagamento de R$ {valor:.2f} via PIX"
#
# RESUMINDO:
#
# Abstração       -> define O QUE precisa ser feito.
# Classe filha    -> define COMO será feito.
# ABC             -> representa uma classe base abstrata.
# @abstractmethod -> cria um comportamento obrigatório nas subclasses.
#
# Relação com os outros pilares:
#
# Encapsulamento -> protege e controla os dados.
# Herança        -> permite reaproveitar características de outra classe.
# Abstração      -> define quais comportamentos são essenciais.
# Polimorfismo   -> permite diferentes implementações desses comportamentos.
#
# Pense no @abstractmethod como um CONTRATO:
# "Se você herdar desta classe, precisa implementar este comportamento."
# ============================================================