"""6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área. """

from cmath import pi

raio = float(input("Informa o raio do círculo em cm: "))

area_circulo = pi * (raio ** 2)

print(f"\nA área do círculo é {area_circulo:0.2f} cm².")