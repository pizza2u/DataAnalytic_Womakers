'''
Contador de Vogais:
Crie uma função chamada contar_vogais que receba uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário que insira uma frase e utilize a função para contar as vogais.
'''

def contar(frase):
    vogais='aeiouAEIOU'
    total_vogais = 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
    return total_vogais

frase_digitada = input("Digite uma frase:\n")
total_vogais = contar(frase_digitada)
print(f"A frase tem {total_vogais} vogais")