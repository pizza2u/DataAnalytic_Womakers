# calcular o tempo de viagem por diferentes meios de transporte

distancia = float(input("Informe a distância do percurso em quilômetros: "))
    
tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80
    
print("Tempo de viagem de avião: %.2f horas.",tempo_aviao)
print("Tempo de viagem de carro: %.2f horas.",tempo_carro)
print("Tempo de viagem de ônibus: %.2f horas.",tempo_onibus)