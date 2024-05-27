notas_escolares = [85, 42, 78, 90, 55, 60, 49, 73, 88, 35]

for nota in notas_escolares:
    if nota > 80:
        print(f"Aluno foi aprovado com certificado: {nota}")
    elif 60 <= nota <= 80:
        print(f"Aluno apenas aprovado: {nota}")
    else:
        print(f"Aluno reprovado: {nota}")

