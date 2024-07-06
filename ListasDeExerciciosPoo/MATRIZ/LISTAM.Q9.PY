#9 - Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na diagonal secundária.

from random import randint


linha= [0]*3
soma=0


for i in range(len(linha)):
    linha[i]= [0]*3
    for t in range(len(linha[i])):
        linha[i][t]= randint(0,20)
        if i+t==2:
            soma+=linha[i][t]
for c in range(len(linha)):
    print(linha[c])
print('O calculo da diagonal secundaria é: ',soma)
