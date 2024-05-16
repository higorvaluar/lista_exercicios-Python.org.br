# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input("Qual o tamanho do seu arquivo? (MB): "))
linkSpeed = float(input("Qual a velocidade da internet? (Mbps): "))
bits = mb * 8 * 10 ** 6
megabits = bits / 10 ** 6
secAprox = megabits / linkSpeed
minAprox = secAprox / 60

print(f"O download levará aproximadamente {minAprox} minuto(s) para ser concluído!")