# calcular o consumo médio de combustível

litros = float(input("Informe a quantidade de litros de combustível consumidos: "))
distancia = float(input("Informe a distância percorrida em quilômetros: "))
    
consumo_medio = distancia / litros
    
print(f"O consumo médio é de {consumo_medio:.2f} km/l.")


