#8 - Faça uma função que aloca uma matriz m × m (quadrada) e preenche com 1 sua diagonal principal e
#com 0 os demais elementos (matriz identidade). Sua função deve receber o valor de m.
'''
from random import randint


linha= [0]*4

for i in range(len(linha)):
    linha[i]=[0]*4
    for t in range(len(linha[i])):
        linha[i][t]= randint(0,50)
        if [i]==[t]:
           linha[i][t]=1
        if [i]!=[t]:
           linha[i][t]=0
print('===A matriz é====')
for t in range(len(linha)):
     print(linha[t])
     '''
'''
linhas=int(input("quantidade de linhas: "))
colunas=int(input("quantidade de colunas: "))
matriz=[0]*linhas

for l in range(len(matriz)):
    matriz[l]=[0]*colunas
    for c in range(len(matriz[l])):
        if l==c:
            matriz[l][c]=1
        else:
            matriz[l][c]=0
for i in range(len(matriz[l])):
        print(matriz[i])
    '''