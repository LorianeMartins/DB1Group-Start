"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações"""

salario_bruto = float(input("Informe o salário bruto em R$: "))

if salario_bruto <= 900:

    imposto_renda = 0

elif 900 < salario_bruto <= 1500:

    imposto_renda = 0.05

elif 1500 < salario_bruto <= 2500:

    imposto_renda = 0.10

else: 
    imposto_renda = 0.20

desconto_ir = salario_bruto * imposto_renda
desconto_sindicato = salario_bruto * 0.03
deposito_fgts = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto_ir - desconto_sindicato

print(f"\nSalário Bruto: R${salario_bruto}")
print(f"Desconto IR: R${desconto_ir}")
print(f"Desconto Sindicato: R${desconto_sindicato}")
print(f"Depósito FGTS : R${deposito_fgts}")
print(f"Salário líquido: R${salario_liquido}")


