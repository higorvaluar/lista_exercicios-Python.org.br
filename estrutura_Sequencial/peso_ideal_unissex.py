# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

sexo = input("Qual é o seu sexo? (M / F): ").upper()
h = float(input("Qual é sua altura? (m): "))

match sexo:
    case "M":
        pIdeal = (72.7 * h) - 58
        print(f"Seu peso ideal é de {pIdeal:.1f} kg")
    case "F":
        pIdeal = (62.1 * h) - 44.7
        print(f"Seu peso ideal é de {pIdeal:.1f} kg")