# lê três números inteiros e os mostre em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
    
numeros = [num1, num2, num3]
numeros.sort()
    
print("Números em ordem crescente:", numeros)