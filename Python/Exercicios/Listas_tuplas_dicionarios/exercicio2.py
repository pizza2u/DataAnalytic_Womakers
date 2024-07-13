# Programa para calcular a média de 5 alunos e imprimir o número de alunos com média maior ou igual a 7.0
medias = []

for i in range(5):
    print(f"Aluno {i + 1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

alunos_acima_7 = sum(1 for media in medias if media >= 7.0)

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_7}")