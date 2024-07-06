#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida
lista=[]

for i in range (0,1):   
    idade = int(input("Informe a sua idade: "))
    altura= float(input("Informe a sua altura: "))
    lista.append({"idade":idade, "altura":altura}.values())
    
for indice, valor in enumerate(lista):
    l=list(valor)
    l.sort()
    print(f"indice {indice} e {l}")
    