# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

F = float(input("Quantos °F estão fazendo agora? "))
C = 5 * ((F-32) / 9)

print(f"{F:.1f}°F é igual a {C:.1f}°C")