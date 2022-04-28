"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo"""

numero = int(input("Informe um número inteiro menor que 1000: "))

unidades = int(numero % 10)
dezenas = int(((numero - unidades) / 10) % 10)
centenas = int((numero - (dezenas * 10) - unidades) / 100)

print(f"UNIDADES -> {unidades}")
print(f"DEZENAS -> {dezenas}")
print(f"CENTENAS -> {centenas}")


