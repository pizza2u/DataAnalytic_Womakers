'''
Reverso de Número:
Crie uma função que retorne o reverso de um número inteiro informado. Por exemplo, para o número 127, o reverso seria 721.
'''

def reverse(numero):
    return int(str(numero)[::-1])

numero = int(input("Digite um número inteiro: "))

result=reverse(numero)
print(result)
