'''
Soma de Três Números:
Escreva um programa que inclua uma função que requer três argumentos e forneça a soma desses três argumentos.

'''
def soma(a, b, c):
    return a + b + c

numeros = []
for i in range(3):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

'''res = sum(numeros)
print(res)'''
resultado = soma(numeros[0], numeros[1], numeros[2])
print(f"A soma dos três números é: {resultado}")