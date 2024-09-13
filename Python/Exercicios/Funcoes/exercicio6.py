'''
Jogo de Forca:
Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta
de uma lista predefinida. A palavra secreta será representada por espaços em branco,
um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. 
Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na
palavra secreta, ela será revelada nas posições correspondentes. 
Se a letra não estiver na palavra, uma mensagem de erro será exibida. 
Após um número máximo de erros, o jogador perde. O jogo continua 
até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
'''

import random

def escolher_palavra():
    palavras = ['kpop', 'pop', 'rock', 'sertanejo', 'funk']
    return random.choice(palavras)

def mostrar_palavra_escondida(palavra, letras_corretas):
    palavra_escondida = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_escondida += letra  # mostra a letra se estiver correta
        else:
            palavra_escondida += '_' # mostra um sublinhado se a letra não foi descobe
    return palavra_escondida # retorna a palavra com letras reveladas e sublinhados

def jogar_forca():
    palavra_secreta = escolher_palavra() # escolhe uma palavra secreta aleatória
    letras_corretas = []
    max_tentativas = 6 
    tentativas = 0 # contador

    print("Bem-vindo ao jogo de Forca!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")

    while tentativas < max_tentativas:
        print("\nPalavra secreta:", mostrar_palavra_escondida(palavra_secreta, letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas += 1 # incrementa o número de tentativas realizadas

        if '_' not in mostrar_palavra_escondida(palavra_secreta, letras_corretas):
            print("\nParabéns! Você acertou a palavra secreta:", palavra_secreta)
            break

    if tentativas >= max_tentativas:
        print("\nGame Over! Você excedeu o número máximo de tentativas.")
        print("A palavra secreta era:", palavra_secreta)

jogar_forca()
