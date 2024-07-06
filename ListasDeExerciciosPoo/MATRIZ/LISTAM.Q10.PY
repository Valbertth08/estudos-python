#10 - Dada a matriz abaixo implemente procedimento que imprima a seguinte matriz:
'''
matriz=[8,0,7],[4,5,6],[3,10,2]

for i in range(len(matriz)):
    print(matriz[i])
'''

vetor= [3,4,5,6,7,8]
vti=[]

for i in range(5,-1,-1):
    vti.append(vetor[i])
print('O valor normal é: ',vetor)
print('O valor inverso é: ',vti)
