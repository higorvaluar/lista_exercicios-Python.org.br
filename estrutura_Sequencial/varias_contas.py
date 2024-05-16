# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo
# b) a soma do triplo do primeiro com o terceiro
# c) o terceiro elevado ao cubo

nI1, nI2 = map(int, input("Digite 2 números inteiros: ").split())
nR = float(input("Digite 1 número real: "))

# Letra A

dobro1 = nI1 * 2
metade2 = nI2 / 2
prod = dobro1 * metade2
print(f"O produto do dobro do primeiro com metade do segundo é {prod} !")

# Letra B

triplo1 = nI1 * 3
soma = triplo1 + nR
print(f"A soma do triplo do primeiro com o terceiro é {soma:.1f}")

# Letra C

cubo3 = nR * nR * nR
print(f"O terceiro elevado ao cubo é {cubo3:.2f}")