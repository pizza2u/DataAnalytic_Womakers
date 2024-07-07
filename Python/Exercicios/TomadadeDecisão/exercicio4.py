#  classifique um aluno com base em sua pontuação em um exame.
nota = float(input("Digite a nota do exame (0 a 10): "))
    
if 0 <= nota <= 10:
    if nota >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
else:
    print("Nota inválida.")