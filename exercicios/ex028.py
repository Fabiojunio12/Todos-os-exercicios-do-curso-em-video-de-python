#Escreva um programa aque faça o computador "penasar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir que foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0, 5) #Faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que nome eu pensei? '))#jogador tenta advinhar!
if jogador == computador:
	print('PARABÉNS! você conseguiu ne ganhar!')
else:
	print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
