# Programa para criar um dicionário representando um carrinho de compras e calcular o total

precos = {
    "arroz": 7.0,
    "feijao": 8.0,
    "macarrao": 5.0,
    "azeite": 30.0,
    "acucar": 3.0
}

print("Lista de produtos disponíveis:")
for produto, preco in precos.items():
    print(f"{produto.capitalize()}: R${preco:.2f}")

carrinho = {}

while True:
    produto = input("\nDigite o nome do produto (ou 'sair' para finalizar): ").strip().lower()
    if produto == 'sair':
        break
    if produto not in precos:
        print(f"Produto '{produto}' não encontrado na lista. Tente novamente.")
        continue
    quantidade = int(input(f"Digite a quantidade de {produto}: "))
    if produto in carrinho:
        carrinho[produto] += quantidade
    else:
        carrinho[produto] = quantidade

total = 0.0
for produto, quantidade in carrinho.items():
    total += quantidade * precos[produto]

print(f"\nTotal do carrinho de compras: R${total:.2f}")
