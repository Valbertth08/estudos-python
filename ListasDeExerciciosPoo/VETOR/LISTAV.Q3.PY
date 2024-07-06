#Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor.
#  Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

from random import randint


vetor= [0]*4
quadrado=[]

for i in range (len(vetor)):
    vetor[i]= float(input('Digite um valor: '))
    quadrado.append(vetor[i]**2)
print('O quadrado dos numeros é: ',quadrado)

