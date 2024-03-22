#metodos 
#union( une dois conjuntos)

conjunto_a={1,2}
conjunto_b={3,4}
print(conjunto_a.union(conjunto_b))

#intersecção (valores iguais nos dois conjuntos)
conjunto_a={1,2}
conjunto_b={2,4}
print(conjunto_a.intersection(conjunto_b))

#diferença (é tudo que eu tenho em um conjunto, que não tem no outro)
conjunto_a={1,2,3}
conjunto_b={2,3,4}
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.difference(conjunto_b))


#symmetric_difference (retorna os dois, tanto o que existe A mais não tem no B e quanto tem no B mais não tem no A)
#valores(que não tem interscção nos conjuntos)
conjunto_a={1,2,3}
conjunto_b={2,3,4}
print(conjunto_b.symmetric_difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))


#issubset
#(se todos os valores de determinado conjunto esta no outro , ou seja, ele subconjunto de outro)
#são retornados valores boleanos, true e false
conjunto_a={1,2,3}
conjunto_b={4,1,2,5,6,3}
print(conjunto_a.issubset(conjunto_b))# todos os elementos de  A estão em B
print(conjunto_b.issubset(conjunto_a)) #verificar se todos os elementos de B estão em A

#issuperset (ao contrario)
conjunto_a={1,2,3}
conjunto_b={4,1,2,5,6,3}
print(conjunto_a.issuperset(conjunto_b))# todos os elementos de  B estão em A?
print(conjunto_b.issuperset(conjunto_a)) #verificar se todos os elementos de A estão em B


#isdisjoint (os elementos de um conjunto é totalmente diferente do outro (sem intersecção))
conjunto_a={1,2,3,4,5,}
conjunto_b={6,7,8,9,}
conjunto_c={1,0}

print(conjunto_a.isdisjoint(conjunto_b))# retrona true
print(conjunto_a.isdisjoint(conjunto_c))#retorna false


#add (adionar um elemneto)obs: ele só adicionado se não existir dentro do set
conjunto_a={1,2,3,4,5,}
conjunto_a.add(30)

#clear(limpar o set)
conjunto_a={1,2,3,4,5,}
conjunto_a.clear()

#copy(copia os elemntos do set)
conjunto_a={1,2,3,4,5,}
conjunto_a.copy()

#discard(descartar um valor do set)
conjunto_a={1,2,3,4,5}
conjunto_a.discard(1)
conjunto_a.discard(45)# se eu tento descartar um valor que não existe no set, ele fica de boa nao da nenhum erro 

#pop( tira os elemntos do set)-so que do começo do conjunto, não do final.
conjunto_a={1,2,3,4,5,}
conjunto_a.pop()#1
conjunto_a.pop()#2

#remove
conjunto_a={0,1,2,3,4,5}
conjunto_a.remove(0) #removendo o elemento do conjutno

#diferença entre o dicard e o remove
#se eu tento remover um elemento que não existe, utiliazando o metodo remove, irar da um erro
# ja no discard não

#len(mostra o tamanho do conjunto)
conjunto_a={0,1,2,3,4,5}
len(conjunto_a)

#in (posso usar para verificar se existe determinado elemento dentro do conjunto)
conjunto_a={0,1,2,3,4,5}
print(0 in conjunto_a)

