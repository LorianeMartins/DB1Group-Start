"""4. Faça um programa que peça as 4 notas bimestrais e mostre a média."""

nota1 = float(input("Informe a nota o 1ºBimestre: "))
nota2 = float(input("Informe a nota o 2ºBimestre: "))
nota3 = float(input("Informe a nota o 3ºBimestre: "))
nota4 = float(input("Informe a nota o 4ºBimestre: "))

media_notas = (nota1 + nota2 + nota3 + nota4) / 4 

print(f"\nA média das notas é {media_notas:0.2f}.")