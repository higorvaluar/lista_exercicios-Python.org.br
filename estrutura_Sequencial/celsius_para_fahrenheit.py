# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input("Quantos °C está fazendo agora? "))
F = (C * 1.8) + 32

print(f"{C:.1f}°C é igual a {F:.1f}°F")