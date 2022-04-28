"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

# Método .split() retorna uma lista de strings separadas a partir de um delimitador como "/"
data = input("Informe uma data no formato dd/mm/aaaa: ")


lista_data = data.split("/")

# Indices e valor correspondente: 0-dia, 1-mês, 2-ano
if data[2] == "/" and data[5] == "/":

    if lista_data[0].isdigit() and lista_data[1].isdigit() and lista_data[2].isdigit(): 

        dia_int = int(lista_data[0])
        mes_int = int(lista_data[1])
        ano_int = int(lista_data[2])

        if 0 < ano_int: 

            # Meses com 31 dias: 
            if (mes_int == 1 or 
                mes_int == 3 or 
                mes_int == 5 or 
                mes_int == 8 or 
                mes_int == 10 or 
                mes_int == 12):

                if 0 < dia_int <= 31:

                    status = True
            
                else:
                    status = False

            # Meses com 30 dias: 
            elif (mes_int == 4 or 
                    mes_int == 6 or 
                    mes_int == 7 or 
                    mes_int == 9 or 
                    mes_int == 11): 

                if 0 < dia_int <= 30: 

                    status = True
            
                else:
                    status = False
        
            # Mês de feveiro, checar se ano é bissexto 
            elif mes_int == 2: 

                # Condição para ser bissexto
                if (ano_int % 4 == 0 and ano_int % 100 != 0) or (ano_int % 400 == 0):

                    if 0 < dia_int <= 29:

                        status = True
                    else:
                        status = False

                elif 0 < dia_int <=28:

                    status = True

                else:
                    status = False
            else: 
                status = False
        else:
            status = False
    else: 
        status = False
else: 
    status = False

print(f"A data é válida? {status}")