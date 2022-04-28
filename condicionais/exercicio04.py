"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input("Informe uma letra: ").upper()

if letra.isalpha() and len(letra) == 1: 

    if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
        
        print(f"{letra} é uma vogal.")
    
    else:
        print(f"{letra} é uma consoante.")
else:
    print(f"{letra} não é válido.")