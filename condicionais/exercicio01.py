"""Faça um Programa que peça dois números e imprima o maior deles. """

numero_a = float(input("Informe um número A: "))

numero_b = float(input("Informe um número B: "))

if numero_a > numero_b:
    print(f"O maior é A: {numero_a}")

elif numero_a == numero_b:
    print(f"Os números são iguais: A = B")

else: 
    print(f"O maior é B: {numero_b}")