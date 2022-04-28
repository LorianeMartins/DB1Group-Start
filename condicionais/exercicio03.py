"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

genero = input("Informe 'F' para 'Feminino' ou 'M' para 'Masculino': ").upper()

if genero == "F":
    print("F - Feminino")

elif genero == "M": 
    print("M - Masculino")

else:
    print("Inválido.")