"""Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada pelo aluno e apresentar:"
A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;

A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez."""

nota_1 = float(input("Informe a nota 1 do aluno: "))
nota_2 = float(input("Informe a nota 2 do aluno: "))

media = (nota_1 + nota_2) / 2

media_minima = 7

if media == 10: 
    print("Aprovado(a) com Distinção.")
elif media_minima < media < 10:
    print("Aprovado(a).")
else:
    print("Reprovado(a).")
