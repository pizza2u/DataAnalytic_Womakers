# conversão de quilômetros


km = float(input("Informe a quantidade de quilômetros: "))
    
metros = km * 1000
centimetros = km * 100000
milimetros = km * 1000000
print("%.0f km é igual a %.0f metros, %.0f centímetros e %.0f milímetros." % (km, metros, centimetros, milimetros))

'''Outras formas de printas
print(f"{km} km é igual a {metros} metros, {centimetros} centímetros e {milimetros} milímetros.")
print("{} km é igual a {} metros, {} centímetros e {} milímetros.".format(km, metros, centimetros, milimetros))
 print(str(km) + " km é igual a " + str(metros) + " metros, " + str(centimetros) + " centímetros e " + str(milimetros) + " milímetros.")
'''
