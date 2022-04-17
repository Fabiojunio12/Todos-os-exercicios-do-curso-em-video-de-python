#crie um programa que leia um número inteiro e mostre na tela se ela é par ou impar.
número = int(input('Me diga um número qualquer: '))
resto = número % 2
if resto == 0:
	print('O número {} é par!'.format(número))
else:
	print('O número {} é impar!'.format(número))
