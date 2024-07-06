#Faça um programa em Python que preencha uma matriz 3x3 de inteiros e escreva:
#) A soma dos números ímpares fornecidos;
#b) A soma de cada uma das 3 colunas;
#c) A soma de cada uma das 3 linhas.

from random import randint


linha= 3
matriz= [0]*linha
impar= []
soma=0
c1=0
c2=0
c3=0
i1=0
i2=0
i3=0
for i in range (len(matriz)):
    matriz[i]=[0]*3
    for t in range (len(matriz[i])):
        matriz[i][t]= randint(0,50)
        if matriz[i][t] %2==1:
         impar.append(matriz[i][t])
        if t==0:
         c1+=matriz[i][t]
        elif t==1:
          c2+=matriz[i][t]
        elif t==2:
          c3+=matriz[i][t]
        if i==0:
          i1+=matriz[i][t]
        elif i==1:
            i2+=matriz[i][t]
        elif i==2:
          i3+=matriz[i][t]
for c in range(len(matriz)):
     print(matriz[c]) 
print('Os numeroes impares são: ',impar)
print('A soma entres os numeros impares são: ',sum(impar))
print('A soma da coluna 0 é: ',c1)
print('A soma da coluna 1 é: ',c2)
print('A soma da coluna 2 é: ',c3)
print('A soma  da linha 0 é: ',i1)
print('A soma  da linha 1 é: ',i2)
print('A soma  da linha 2 é: ',i3)
 
