# calcular e apresentar a quantidade de números pares e ímpares inseridos.
pares = 0
impares = 0
    
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    elif numero > 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
