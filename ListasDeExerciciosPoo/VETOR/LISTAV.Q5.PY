#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na
#ordem inversa.
inverso= []
vetor= [2,4,5,6,7,8,9,10]


for i in range(7, -1, -1): 
    inverso.append(vetor[i])
print(inverso)


    