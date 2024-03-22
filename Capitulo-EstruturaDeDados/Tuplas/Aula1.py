#Criando uma tupla

frutas=("larnja","pera","uva",)# preciso colocar uma ultima virgula no final. para o compilador não confundir se é uma ordem de precednecia ou uma tupla
letras=tuple("python")# criando com o construtor, cada letra é um elemento da tupla

numeros=tuple([1,2,4,5])
pais=("Brasil",)#sempre colocar a virgula o final

#acessando os elementos de uma tupla
frutas=("larnja","pera","uva",)
frutas[0]
frutas[2]
frutas[-3]

#tuplas aninhada(tupla, dentro de outra tupla)

matriz=(
    (1,"a",1),
    ("b",3,4),
    (6,5,"c")
)
matriz[0] #(1,"a",1)
matriz[0][0] #1

#fatiamento# mesmas formas da lista
frutas=("p","y","t","h","o","n",)
frutas[2:]# pego o valor da posição doi até o resto da string
frutas[:2]# pego o valor até a posição 2 da lista
frutas[1:3]# começa da posição 1 e vai até a posição 3
frutas[0:3:2]# começa da posição 0 vai até o 3 pulando de 2 em 2
frutas[::-1]#pulando de 1 em um na ordem inversa
frutas[::]#é feito uma copia da tupla, não fatia nada (vazio,vazio,vazio)

#metodos
#count
frutas=("laranja","pera","uva","laranja")
frutas.count("laranja") #conta quantaas vezes determinado elemento se repete na tupla

#index
frutas=("laranja","pera","uva","laranja")
frutas.index("uva")# saber qual posição se encontra determinado elemento 

#len
len(frutas)# mostra quantos elementos tem dentro da tupla

