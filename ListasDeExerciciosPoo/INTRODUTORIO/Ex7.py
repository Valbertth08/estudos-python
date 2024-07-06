#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista=[1,2,3,4,5]
soma=0
mult=1
for i in lista:
    soma+=i
for i in lista:
    mult*=i
print(soma)
print(mult)


