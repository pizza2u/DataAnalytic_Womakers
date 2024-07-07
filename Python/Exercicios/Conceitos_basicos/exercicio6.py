# calcular o IMC
peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros: "))
    
imc = peso / (altura * altura)
    
print(f"O seu IMC é {imc:.2f}.")