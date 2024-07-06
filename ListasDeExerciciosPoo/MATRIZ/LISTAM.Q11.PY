#Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada
#linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária
#são todas iguais. Dada a matriz da questão 10 verificar se a mesma é uma quadrado mágico.

matriz=[8,0,7],[4,5,6],[3,10,2]
l0=0
l1=0
l2=0
c0=0
c1=0
c2=0

for i in range(len(matriz)):
    print(matriz[i])
    for t in range(len(matriz[i])):
        if i==0:
            l0+=matriz[i][t]
        elif i==1:
            l1+=matriz[i][t]
        elif i==2:
            l2+=matriz[i][t]
        if t==0:
                c0+=matriz[i][t]
        elif t==1:
            c1+=matriz[i][t]
        elif t==2:
            c2+=matriz[i][t]
print('A soma dos valores são',l0,l1,l2,c0,c1,c2)