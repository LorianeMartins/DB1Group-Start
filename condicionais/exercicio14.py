""" Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno."""

lado_1 = float(input("Informe o valor do lado 1 do triângulo em cm: "))
lado_2 = float(input("Informe o valor do lado 2 do triângulo em cm: "))
lado_3 = float(input("Informe o valor do lado 3 do triângulo em cm: "))

lados = []

lados.append(lado_1)
lados.append(lado_2)
lados.append(lado_3)

maior_valor = max(lados)

lados.remove(maior_valor)

soma = sum(lados)

if soma > maior_valor: 

    print("\nOs valores formam um triângulo.")

else:
    print("\nOs valores não formam um triângulo.")




