#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
ano = int(input('Quantos anos de financiamento: '))
prestação = casa / (ano * 12)
mínimo = salário * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
	print('Emprestimo pode ser .CONCEDIDO!')
else:
	print('Emprestimo NEGADO!')
