'''
1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:""Telefonou para a vítima?""""Esteve no local do crime?""""Mora perto da vítima?""""Devia para a vítima?""""Já trabalhou com a vítima?""

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"",entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"".Caso contrário,ele será classificado como ""Inocente"".
'''

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []
print("Iremos começar o interrogatório\n")
for pergunta in perguntas:
    while True:
        resposta = input(pergunta + " (S/N): ").strip().lower()
        if resposta in ["s", "n"]:
            respostas.append(resposta)
            break
        else:
            print("Por favor, responda com 'S' ou 'N'.")

contador_sim = respostas.count("s")

if contador_sim == 5:
    classificacao = "Assassino"
elif 3 <= contador_sim <= 4:
    classificacao = "Cúmplice"
elif contador_sim == 2:
    classificacao = "Suspeito"
else:
    classificacao = "Inocente"

print("\nClassificação:", classificacao)