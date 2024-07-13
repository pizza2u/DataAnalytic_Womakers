#  Programa para criar um dicionário de contatos e permitir a busca por nome
# Dicionário para armazenar os contatos
contatos = {}

# Loop para adicionar contatos
while True:
    nome = input("Digite o nome do contato (ou 'sair' para finalizar): ").strip().lower()
    if nome == 'sair':
        break
    telefone = input(f"Digite o telefone de {nome}: ")
    contatos[nome] = telefone


nome_contato = input("\nDigite o nome do contato que deseja procurar: ").strip().lower()
telefone = contatos.get(nome_contato, "Contato não encontrado.")
print(f"Telefone de {nome_contato}: {telefone}")