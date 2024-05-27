def verificar_aprovacao(nome, idade, nota1, nota2, nota3):
    # Somar as notas
    soma_notas = nota1 + nota2 + nota3
    
    # Verificar se a soma das notas é maior ou igual a 60
    if soma_notas >= 60:
        print(f"O aluno {nome}, de {idade} anos, passou de ano!")
    else:
        print(f"O aluno {nome}, de {idade} anos, não passou de ano.")

# Exemplo de uso da função
verificar_aprovacao("sinthya", 16, 90, 40, 100)





