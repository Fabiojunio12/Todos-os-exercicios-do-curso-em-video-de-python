'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
-1 para binário
-2 para octal
-3 para hexadecinal
'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
	[1]converter para BINÁRIO
	[2]converter para OCTAL
	[3]converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
	print('{} convertido a binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
	print('{} convertido a octal é {}' .format(num, oct(num)[2:]))
elif opção == 3:
	print('{} convertido a hexadecinal é {}'.format(num, hex(num)[2:]))
else:
	print('opção inválida. Tente novamente!')
