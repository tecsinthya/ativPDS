notas_escolares = [85, 42, 78, 90, 55, 60, 49, 73, 88, 35]

# Iterar sobre cada nota na lista
for nota in notas_escolares:
    # Verificar se a nota é maior ou igual a 60
    if nota >= 60:
        print(f"Aprovado: {nota}")
    else:
        print(f"Reprovado: {nota}")

