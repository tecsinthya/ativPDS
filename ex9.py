 # Definindo a lista de notas
notas = [60, 55, 80, 90, 59, 30]

# Definindo a função para determinar se a nota é maior ou igual a 60 ou menor
def verificar_nota(nota):
    if nota >= 60:
        print("A nota", nota, "é maior ou igual a 60.")
    else:
        print("A nota", nota, "é menor que 60.")

# Testando a função para cada nota na lista
for nota in notas:
    verificar_nota(nota)
