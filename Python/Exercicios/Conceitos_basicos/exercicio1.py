# Faça um Programa que peça dois números,realize as principaiso perações soma,subtração,multiplicação,divisão
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
    
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
if num2 != 0:
   divisao = num1 / num2
else:
   divisao = "Divisão por zero não é permitida"

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


# Ou com def 
'''
def operacoes_basicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Divisão por zero não é permitida"

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

operacoes_basicas()
'''