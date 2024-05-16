# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_PorHora = float(input("Quanto você ganha por hora trabalhada? R$"))
horasTrabalhadas = int(input("Trabalhou por quantas horas no mês? "))

salario = ganho_PorHora * horasTrabalhadas

print(f"Seu salário do mês será de {salario:.2f} reais!")