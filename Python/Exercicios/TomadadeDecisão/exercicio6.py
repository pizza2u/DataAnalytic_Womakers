# solicite a usuário um login e uma senha.

login = input("Digite o login: ")
senha = input("Digite a senha: ")
    
if login == "admin" and senha == "admin123":
    print("Acesso permitido.")
else:
    print("Login ou senha incorretos.")