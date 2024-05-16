# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido.

print("------------------------------------")
porHora = float(input("Quanto você ganha por hora? R$"))
horaTrab = int(input("Você trabalhou por quantas horas no mês? (h): "))
print("------------------------------------")
salario = porHora * horaTrab
impRenda = salario * 0.11
inss = salario * 0.08
sind = salario * 0.05
salLiquid = salario - (impRenda + inss + sind)

print(f"+ Salário Bruto: R${salario:.2f} \n- Imposto de Renda (11%): R${impRenda:.2f} \n- INSS (8%): R${inss:.2f} \n- Sindicato (5%): R${sind:.2f} \n= Salário Líquido: R${salLiquid:.2f}")
print("------------------------------------")