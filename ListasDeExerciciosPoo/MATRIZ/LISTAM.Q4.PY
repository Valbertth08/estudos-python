#Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X
#e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
#deverá escrever a soma dos valores encontrados nas respectivas posições X e Y .
vetor= [12,15,60,54,89,43,23,55]
soma=0
x= int(input('Digite a cooerdenadada da posição que você que saber: '))
y= int(input('Digite a segunda cooerdenada da posição que você quer saber: '))
soma+=vetor[x]+vetor[y]
print('A soma enre {x} e {y} é:{soma}')