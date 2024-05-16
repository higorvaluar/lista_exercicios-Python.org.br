# 4. Digite 4 notas do bimestre e calcule sua média, depois imprima!

n1, n2, n3, n4 = map(float, input("Adicione as 4 notas dos bimestres: ").split())

media = (n1 + n2 + n3 + n4) / 4

print(f"A média dos 4 bimestres é {media}")