# Dado o seguinte vetor [1,2,4,16,32,64,-128] 
# implemente um procedimento que indique o menor e o maior elemento do vetor. 

vetor= [1,2,4,16,32,64,-128]
maior= 0
menor= 0

for i in range(0,7):
  if i ==0:
      maior= vetor[i]
      menor= vetor[i]
  elif vetor[i]>maior:
       maior= vetor[i]
  elif vetor[i]<menor:
       menor= vetor[i]
print('O maior valor é: ',maior)
print('O menor valor é: ',menor)