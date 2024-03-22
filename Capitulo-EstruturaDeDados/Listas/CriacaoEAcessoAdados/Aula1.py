#declaração
frutas =["banana","maça","melão"]
frutas=[]# posso ter uma lista vazia
letras=list("python")# usando o construtor# cada letra vai ser um elemento da lista
carro=["Ferrari","F8",23455,True]# pode receer diferente tipos

#Acesso

frutas[0]#pegando o valor pelo indice 
frutas[-1]#para pegar o ultimo elemento da lista, basta colocar -1(pegar qualquer valor de forma contraria, basta colocar de forma negativa)

#Lista Aninhada

matriz=[[1,3],[1,6,7],[12,45,5]]
matriz[0][0]# pegando o valor 0 da linha 0
matriz[0][-1]# pegando o valor da linha zero da ultima posição 

#Fatiamento
lista=["p","y","t","h","o","n"]
lista[2:]# pego o valor da posição doi até o resto da string
list[:2]# pego o valor até a posição 2 da lista
lista[1:3]# começa da posição 1 e vai até a posição 3
lista[0:3:2]# começa da posição 0 vai até o 3 pulando de 2 em 2
lista[::-1]#pulando de 1 em um na ordem inversa
lista[::]#é feito uma copia da lista, não fatia nada (vazio,vazio,vazio)

#OBS: O STOP NÃO É INLCUSO, OU SEJA, SE EU DIGO QUE O VALOR É ATÉ 3, NA VDD ELE VAI ATÉ 2

#Percorrer uma Lista
frutas =["banana","maça","melão"]
for fruta in frutas:
    print(fruta)

#Função Eumerate
#Me retorna dois valores, o indice da iteração e o valor associado a ele
for indice,frutas in enumerate(frutas):
    print(f"{indice}: {carro}")


#Compreensão de Listas 
#Filtro 1
numeros=[1,30,21,2,9,65,34]
pares=[]
for numero in numeros:
    if(numero) %2 ==0:
        pares.append(numero)
print(pares)

#Comprerange
numeros=[1,30,21,2,9,65,34]
pares=[numero for numero in numeros if numero % 2 ==0   ] # pares[retorno(obrigatoria),for(obrigatoria),condição(opcional)] como ta dentro do de uma lista, automatiamente os valores retornados são inseridos

#Modificando os valores
numeros=[1,30,21,2,9,65,34]
quadrado=[]
for numero in numeros:
    if(numero) %2 ==0:
        quadrado.append(numero**2)
print(quadrado)
#Modificando os valores(comprerange)
quadrado=[numero **2 for numero in numeros]

