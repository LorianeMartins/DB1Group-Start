"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. """

valor = float(input("Informe um valor: "))

if valor < 0: 
    print(f"O valor {valor} é negativo.")
elif valor == 0:
    print("Zero é zero!")
else:
    print(f"O valor {valor} é positivo.")