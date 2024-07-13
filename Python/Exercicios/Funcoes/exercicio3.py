''''Conversor de Temperatura:
Desenvolva um script que pergunte ao usuário se ele deseja converter uma
temperatura de graus Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função correspondente. 
Além disso, crie um menu onde o usuário possa escolher a opção desejada.'''

def celsius2fahr(celsius):
    return (celsius * 9/5) + 32

def fahr2celsius(fahr):
    return (fahr-32) * 5/9

def menu():
    print("\nMenu:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    choice = input("Opção: ")

    if choice == '1':
        temperatura_cel= float(input("Digite a temperatura em Celsius: \n"))
        result = celsius2fahr(temperatura_cel)
        print(f"{temperatura_cel} ºC é igual a {result:.2f} ºF\n")
    elif choice == '2':
        temperatura_fah= float(input("Digite a temperatura em Fahrenheit: \n"))
        result = fahr2celsius(temperatura_fah)
        print(f"{temperatura_fah} ºF é igual a {result:.2f} Cº\n")   
    else:
        print("Inválido") 


menu()
 