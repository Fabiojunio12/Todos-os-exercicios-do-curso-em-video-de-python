#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento. Para o salário superior a R$1.250,00, calcule um aumento de 10%. para os inferiores ou iguais, o aumento e de 15%.
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1200:
	novo = salário + (salário * 15 / 100)
else :
	novo = salário + (salário * 10 / 100)
print('Quem ganhavá R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))
