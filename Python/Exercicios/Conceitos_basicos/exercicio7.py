# calcular o salário mensal
ganho_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
    
salario_mensal = ganho_por_hora * horas_trabalhadas
    
print(f"O seu salário no referido mês é R$ {salario_mensal:.2f}.")