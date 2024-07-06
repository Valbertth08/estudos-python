#Dado o vetor do exemplo anterior implemente o procedimento que calcule a soma dos
#elementos do vetor.

vetor= [1,2,4,16,32,64,-128]
soma=0


for i in range(0,7):
   soma+=vetor[i]
print('A soma dos valores é: ',soma)