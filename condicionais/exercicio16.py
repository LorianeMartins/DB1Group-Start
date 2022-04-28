"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."""

ano = int(input("Informe um ano: "))

if ano % 400 == 0:

    status = True

elif ano % 100 == 0:

    status = False

elif ano % 4 ==0:
    
    status = True
else:
    status = False

print(f"{ano} é bissexto? {status}")
