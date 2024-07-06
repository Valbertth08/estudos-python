#- Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
from random import randint


linha= [0]*4
maior= 0


for i in range(len(linha)):
    linha[i]= [0]*4
    for t in range(len(linha[i])):
        linha[i][t]= randint(0,20)
        if linha[i][t] > 10:
            print(linha[i][t])
            maior+=1
for c in range(len(linha)):
    print(linha[c])
print('A quantidade de valores maiores que 10 são: ',maior)

