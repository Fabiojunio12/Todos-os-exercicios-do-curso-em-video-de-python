'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
-até 9 anos: MIRIM
-até 14 anos: INFANTIL
-até 19 anos: Junior
-até 25 anos: SÉNIOR
-acima: MASTER
'''from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
	print('Classificação: MIRIM')
elif idade <= 14:
	print('Classificação: INFANTIL')
elif idade <= 19:
	print('Classificação: JUNIOR')
elif idade <= 25:
	print('Classificação: SENIOR')
else:
	print('Classificação: MASTER')
