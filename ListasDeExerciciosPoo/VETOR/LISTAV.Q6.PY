#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
#os números.
from random import randint


vetor=[0]*5
soma= 0
mult= 1

for i in range(len(vetor)):
    vetor[i]= randint(0,50)
    soma+=vetor[i]
    mult*=vetor[i]
print('Os vetores',vetor)
print('A soma é:',soma)
print('A multiplicação é:',mult)
