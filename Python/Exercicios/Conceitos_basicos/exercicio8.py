# calcular calorias queimadas

horas_exercicio = float(input("Informe o número de horas de exercício físico por semana: "))
minutos_exercicio_por_mes = horas_exercicio * 60 * 4
calorias_queimadas = minutos_exercicio_por_mes * 5
    
print(f"O total de calorias queimadas em um mês é {calorias_queimadas} calorias.")