#Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e da coluna de cada
#elemento. Em seguida, imprima na tela a matriz.

from random import randint


linha=4
matriz=[0]*linha
mult=[0]*linha
for i in range (len(matriz)):
    matriz[i]=[0]*4
    mult[i]=[0]*4
    for t in range(len(matriz[i])):
        matriz[i][t]= randint(0,7)
        mult[i][t]= matriz[i][t]*matriz[i][t]
print('Os valores da matrizes são: ')
for k in range(len(matriz)):
    print(matriz[k])
    
print('A matriz com os valores multiplicados é: ')
for c in range(len(matriz)):
    print(mult[c])


    
    



