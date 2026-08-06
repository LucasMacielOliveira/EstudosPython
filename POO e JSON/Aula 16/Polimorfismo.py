# POLIMORFISMO:
# É quando objetos diferentes recebem o mesmo comando,
# mas cada objeto executa esse comando do seu próprio jeito.
#
# Exemplo:
# cachorro.emitir_som() -> "Au au!"
# gato.emitir_som()     -> "Miau!"
#
# O método é o mesmo: emitir_som()
# O comportamento muda dependendo do objeto.
#
# RESUMINDO:
# Mesmo comando + objetos diferentes + comportamentos diferentes.


#EX 

class Cachorro:

    def emitir_som(self):
        return "Au au!"


class Gato:

    def emitir_som(self):
        return "Miau!"


class Vaca:

    def emitir_som(self):
        return "Muuu!"

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()


animais = [
    Cachorro(),
    Gato(),
]

for animal in animais:
    print(animal.emitir_som())