"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento."""

salario = float(input("Informe o salário em R$: "))

if salario < 280: 

    aumento_percentual = 0.20

elif 280 <= salario < 700: 

    aumento_percentual = 0.15

elif 700 <= salario < 1500: 

    aumento_percentual = 0.10

else: 
    aumento_percentual = 0.05

aumento_valor = salario * aumento_percentual

novo_salario = salario + aumento_valor

print(f"\nO salário antes do reajuste era de R${salario}")
print(f"O aumento foi de {aumento_percentual * 100: 0.2f} %")
print(f"O valor do aumento foi de R${aumento_valor: 0.2f}")
print(f"O novo salário é de R${novo_salario}")


