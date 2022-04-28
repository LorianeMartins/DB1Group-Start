"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

numero_1 = float(input("Informe um primeiro número: "))
numero_2 = float(input("Informe um segundo número: "))
numero_3 = float(input("Informe um terceiro número: "))

numeros = []

numeros.append(numero_1)
numeros.append(numero_2)
numeros.append(numero_3)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
