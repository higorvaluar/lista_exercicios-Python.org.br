# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaPintar = float(input("Digite o tamanho da área a ser pintada (m): "))
metrosPorLata = 18 * 3
latasNecessarias = areaPintar / metrosPorLata

if latasNecessarias != int(latasNecessarias):
    latasNecessarias = int(latasNecessarias) + 1
else:
    latasNecessarias = int(latasNecessarias)

total = latasNecessarias * 80.00

print(f"Você precisará de {latasNecessarias} latas de tinta. \nValor total: R${total:.2f}")