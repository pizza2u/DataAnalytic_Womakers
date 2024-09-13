# Programa para mostrar o nome do usuário de trás para frente em letras maiúsculas

nome = input("Digite o seu nome: ").strip()

nome_invertido = nome[::-1].upper()

print(f"Nome invertido: {nome_invertido}")