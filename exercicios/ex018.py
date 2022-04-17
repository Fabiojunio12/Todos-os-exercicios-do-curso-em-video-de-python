#faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tângete desse ângulo.
from math import sin, cos, tan, radians

ângulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
coseno= cos(radians(ângulo))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
