#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

valores=[]
pares=[]
impares=[]
for  i in range(0,2):
    valor= int(input("informe o valor"))
    valores.append(valor)
    if(valor%2 ==0):
        pares.append(valor)
    else:
        impares.append(valor)
print("Valores: ",valores)
print("Pares: ",pares)
print("Impares: ",impares)
    