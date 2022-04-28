"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

numero_1 = float(input("Informe um primeiro número: "))
numero_2 = float(input("Informe um segundo número: "))
numero_3 = float(input("Informe um terceiro número: "))

numeros = []

numeros.append(numero_1)
numeros.append(numero_2)
numeros.append(numero_3)

numeros_ordenados = sorted(numeros)
numeros_ordenados.reverse()
print(numeros_ordenados)
