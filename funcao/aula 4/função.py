#1 - >Para declara uma função em python usamos "def"

#EXEMPLO

def mensagem ():
    print("olá lucas!")


mensagem()

#2 -> PARAMETROS E ARGUMENTOS

#PARAMETROS E ARGUMENTOS SÃO INFORMAÇÕES QUE A FUNÇÃO RECEBE!

#EXEMPLO

def cumprimento(nome):
    print(f"olá {nome}")

cumprimento("lucas")

#3 - > Funções com RETURN devolvem um resultado

#exemplo

def calcularTotal(preco, quantidade):
    total = preco * quantidade;
    return total    


valor_total = calcularTotal(50,5)

print(valor_total)

#################################

def somar(num1, num2):
    return num1 + num2

resultado = somar(5,6)

print(resultado)


#------------------------#

def calcularValorFinal (valor_total):
    if valor_total < 500:
        percentual = 0
    elif valor_total < 1000:
        percentual = 0.05
    else:
        percentual = 0.10   

    valor_desconto = valor_total * percentual
    valor_final = valor_total - valor_desconto

    return valor_final

resultado = calcularValorFinal(500)

print(resultado)