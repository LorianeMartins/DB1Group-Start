"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c """

a = float(input("Informe um valor para o parâmetro `a` da equação: "))
b = float(input("Informe um valor para o parâmetro `b` da equação: "))
c = float(input("Informe um valor para o parâmetro `c` da equação: "))

delta = (b ** 2) - 4 * a * c

if a != 0: 

    if delta < 0: 

       print("\nNão existe solução no conjunto dos números reais.")

    else: 

        raiz_1 = ((- b) + (delta * (1 / 2))) / (2 * a)
        raiz_2 = ((- b) - (delta * (1 / 2))) / (2 * a)

        print(f"\nRAIZ 1 -> {raiz_1:0.2f}")
        print(f"\nRAIZ 2 -> {raiz_2:0.2f}")

else: 
    print("O valor de 'a' não pode ser 0.")

