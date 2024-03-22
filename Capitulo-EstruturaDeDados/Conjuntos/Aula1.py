#formas de criação de um set 
set([1,2,3,2,3,6]) #utilizando  o construtor
lista={1,3,4,3} # ou passando as chaves {}
print(lista)

set([1,2,3,2,3,6])# elimna os elementos duplicados da lista
set("abacaxi")# elimina também da string(porque string é um elemento iteravel)
set(( "palio","gol","palio"))#eliminando da tupla


#acessando dados do set  ( não tem como acessar o indice)
#É preciso fazer uma conversão do set para uma lisya
#ex:
numeros={1,2,4,5,2}
lista=list(numeros)
numeros[0]

#percorrendo o set 
for i in numeros:
    print(i)