
 # Definindo a lista de notas
notas = [0]

# Alterando o valor da primeira nota para 80
notas[0] = 80

# Adicionando as notas 60, 30, 40, 80, 90
notas.append(60)
notas.append(30)
notas.append(40)
notas.append(80)
notas.append(90)

# Imprimindo o array
print("Notas após adicionar novos elementos:", notas)

# Removendo os 2 últimos elementos
notas.pop()
notas.pop()

# Imprimindo novamente o array após remover os 2 últimos elementos
print("Notas após remover os dois últimos elementos:", notas)

