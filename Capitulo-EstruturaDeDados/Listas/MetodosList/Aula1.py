
#Append(armazenar um valor na lista )
Lista=[]
Lista.append(20)

#Clear(limpar a lista )
Lista.clear()

#Copy(retonra uma lista em uma instancia diferente da original, ou seja, uma nova lista baseado na antiga)
#entretando caso eu não faço isso, a mudança que eu faria na lista1, afetaria também na lista 2
Lista1=["rogerio",20,"raimundo","felipe"]
l2=Lista1.copy()
print(id(Lista1),id(l2))

#count(conta quando elementos repetidos existem dentro da lista), passando um valor para o count
cores=["vermelho","azul","verde","azul"]
print(cores.count("azul"))

# Extend -uma forma de juntar duas listas(mesmo que exista elemtnos iguais tudo vai ser junstado(merge))
cores=["vermelho","azul","verde","azul"]
cores.extend(["preto"])
print(cores)

#index(retorna a posição do elemento dentro da lista)# obs: ele pega a primeira ocorrencia do elemento
print(cores.index("vermelho"))

#pop("remeove e retorna o ultimo elemnto da lista") ela vem como uma pilha(o ultimo a entra é o primeiro a sair)
cores=["vermelho","azul","verde","azul"]
cores.pop()
cores.pop()
cores.pop(0)# posso passar um indice par remover o elemento tbm

#remove(tambem é uma forma de remover um elemento de uma lista, entretando inves de passa o indice, é baixado objeto em si para função)
cores=["vermelho","azul","verde","azul"]
cores.remove("azul")
#OBS: ele também só tira uma ocorrencia do elemento 

#reverse(serve para inverter a lista)
cores=["vermelho","azul","verde","azul"].reverse()
print(cores)

#sort(ordenada a lista de ordem alfabetica por padrão )
cores=["vermelho","azul","verde","azul"].sort()

#funções dentro do sort

#reverse (0ordena ao contreario, do maior par ao menor)
cores=["vermelho","azul","verde","azul"].sort(reverse=True)
#Estou mundando a forma de ordenação, utilizando uma expressão lambda que ordena as palavas pelo o numero de carateres(pegando do menor para o maior)
cores=["vermelho","azul","verde","azul"].sort(key=lambda x: len(x))

#Estou mundando a forma de ordenação, utilizando uma expressão lambda que ordena as palavas pelo o numero de carateres(pegando do maior para o menor)
cores=["vermelho","azul","verde","azul"].sort(key=lambda x: len(x),reverse=True)

#len(pega o tamanho da lista)
cores=["vermelho","azul","verde","azul"]
print(len(cores))

#sorted (receebe dois parametros (iteravel(obrigatorio),expressão lambda(opcional), reverse(opcional))) mesma coisa do sort, a diferença é que ele é uma função
sorted(cores,key=lambda x: len(x))
sorted(cores,key=lambda x: len(x),reverse=True)
sorted(cores)# por padrão, ordena em ordem alfabetia




