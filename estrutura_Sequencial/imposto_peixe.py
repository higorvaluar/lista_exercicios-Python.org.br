# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Quantos quilo(s) de peixe você trouxe da pesca? "))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print()
    print(f"A pesca teve um excesso de {excesso:.2f} quilo(s). \nA multa será de R${multa:.2f}!")
else:
    print()
    print(f"O senhor pescou {peso:.2f} quilo(s) de peixe \nSendo assim não terá multa!")