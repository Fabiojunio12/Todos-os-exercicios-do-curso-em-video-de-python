#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 11)
if computador == 0:# pedra
	if jogador == 0:
		print('EMPATE!')
	elif jogador ==  1:
		print('JOGADOR GANHOU!')
	elif jogador == 2:
		print('COMPUTADOR GANHOU!')
	else:
		print('JOGADA INVÁLIDA! tente novamente!')
elif computador == 1: # papel
	if jogador == 0:
		print('COMPUTADOR GANHOU!')
	elif jogador == 1:
		print('EMPATE!')
	elif jogador == 2:
		print('JOGADOR GANHOU!')
	else:
		print('JOGADA INVÁLIDA! tente novamente.')
elif computador == 2:# tesoura
	if jogador == 0:
		print('JOGADOR GANHOU!')
	elif jogador == 1:
		print('COMPUTADOR GANHOU!')
	elif jogador == 2:
		print('EMPATE!')
	else:
		print('JOGADA INVÁLIDA! tente novamente.')
		