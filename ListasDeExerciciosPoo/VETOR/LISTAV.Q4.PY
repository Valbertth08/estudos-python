#Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X
#e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
#deverá escrever a soma dos valores encontrados nas respectivas posições X e Y

vetor= [4,5,69,19,5,6,7,8]
soma= 0

x= int(input('Digite um valor: '))
y= int(input('Digite um valor: '))
soma= vetor[x]+vetor[y]
print(soma)