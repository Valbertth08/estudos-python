#Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na
#matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.
from random import randint


matriz=[0]*4
x= int(input('Digite um valor para ser buscado: '))
for i in  range(len(matriz)):
    matriz[i]= [0]*4
    for t in range(len(matriz[i])):
        matriz[i][t]= randint(0,50)
        if matriz[i][t]== x :
          print(f'O  valor estar na linha {i} e na coluna {t}')
else:
    print('Valor não encontrado')
for c in range(len(matriz)):
    print(matriz[c])


        


    