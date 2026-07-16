senha_Correta = "123456"
senha_digitada= ""

while senha_digitada != senha_Correta:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_Correta:
        print("Senha correta! Acesso permitido.")
    else:
        print("Senha incorreta! Tente novamente.")