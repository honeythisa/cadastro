# Recebe 5 valores do usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
valor4 = float(input("Digite o quarto valor: "))
valor5 = float(input("Digite o quinto valor: "))

# Define os pesos de cada valor (neste caso, iguais)
peso1 = valor1/(valor1 + valor2 + valor3 + valor4 + valor5)
peso2 = valor2/(valor1 + valor2 + valor3 + valor4 + valor5)
peso3 = valor3/(valor1 + valor2 + valor3 + valor4 + valor5)
peso4 = valor4/(valor1 + valor2 + valor3 + valor4 + valor5)
peso5 = valor5/(valor1 + valor2 + valor3 + valor4 + valor5)

# Calcula a média ponderada
media_ponderada = ((valor1*peso1) + (valor2*peso2) + (valor3*peso3) + (valor4*peso4) + (valor5*peso5)) / 5

# Imprime o resultado
print("A média ponderada é:", media_ponderada)