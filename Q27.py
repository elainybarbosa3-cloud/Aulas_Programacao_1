usuario_correto = "Mikely"
senha_correta = "123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha inválidos.")