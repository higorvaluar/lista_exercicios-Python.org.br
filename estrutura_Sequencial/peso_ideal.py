# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:        (72.7*altura) - 58

altura = float(input("Qual é sua altura? (m): "))

pIdeal= (72.7 * altura) - 58

print(f"Seu peso ideal é de {pIdeal:.1f} kg")