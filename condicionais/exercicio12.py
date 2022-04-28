"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.""" 

numero_dia = input("Informe um número de 1 a 7: ")

if numero_dia.isdigit(): 

    inteiro_num_dia = int(numero_dia)

    if inteiro_num_dia < 1 or inteiro_num_dia > 7:

        print("Número inválido.") 
    
    elif inteiro_num_dia == 1:

        print("Domingo")

    elif inteiro_num_dia == 2:
        
        print("Segunda")
    
    elif inteiro_num_dia == 3:
        
        print("Terça")

    elif inteiro_num_dia == 4:
        
        print("Quarta")
    
    elif inteiro_num_dia == 5:
        
        print("Quinta")
    
    elif inteiro_num_dia == 6:
        
        print("Sexta")

    elif inteiro_num_dia == 7:

        print("Sábado")

else: 
    print("Valor inválido.")