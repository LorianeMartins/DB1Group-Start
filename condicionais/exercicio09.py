"""Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso"""

turno = input("Digite 'M' para 'Matutino', 'V' para 'Vespertino' ou 'N' para 'Noturno': ").upper()

if turno.isalpha() and len(turno) == 1:

    if turno == "M":

        print("Bom dia!")

    elif turno == "V":

        print("Boa tarde!")
    
    elif turno == "N":

        print("Boa noite!")

    else: 

        print("Letra inválida.")

else:

    print("Inválido.")