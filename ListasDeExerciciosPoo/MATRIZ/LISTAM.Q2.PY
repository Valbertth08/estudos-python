#Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva
#ao final a matriz obtida.

from operator import iadd
from random import randint


linha= [0]*5

for i in range(len(linha)):
    linha[i]=[0]*5
    for t in range(len(linha[i])):
        linha[i][t]= randint(0,50)
        if [i]==[t]:
           linha[i][t]=1
        if [i]!=[t]:
           linha[i][t]=0
for c in range(len(linha)):
    print(linha[c])
        
