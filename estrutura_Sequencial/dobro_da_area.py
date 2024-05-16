# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

raio = float(input("Digite um valor para o raio do círculo: "))
pi = 3.14159
area = (pi * raio * raio) * 2
print(f"O dobro da área do círculo é {area:.2f}")