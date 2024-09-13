'''
Conversor de Moedas:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e calcule quanto ela poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:

Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suíço: R$0,42
Euro: R$5,36
Libra Esterlina: R$6,21
'''

def calcular_moedas(dinheiro):
    taxa_conversao = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suíço': 0.42,
        'Euro': 5.36,
        'Libra Esterlina': 6.21
    }

    for moeda, taxa in taxa_conversao.items():
        valor_convertido = dinheiro / taxa
        print(f"Com R${dinheiro:.2f} você pode comprar aproximadamente {valor_convertido:.2f} {moeda}")

dinheiro_na_carteira = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))
calcular_moedas(dinheiro_na_carteira)
