
#CLEAR(apaga todo o dicionario )
contatos={
    "jose@gmail.com":{"nome":"jose","telefone":"333-000"},
    "pedro@gmail.com":{"nome":"pedro","telefone":"333-000"}
}

#COPY(copia todo o dicionario para outro ) isso, é um dicionario totalmente do original
copia=contatos.copy()

#FROMKEYS(cria chaves para o meu dicionario )

dict.fromkeys(["nome","telefone"])# estou criando duas chaves para o dicionario, sem passar nenhum valor associado a elas
#obs: essa forma é normalmene utilizada para um dicionario inexistente 

dict.fromkeys(["nome","telefone"],"vazio")# estou criando duas chaves e atribuindo o valor "vazio", a elas(valor padrão)
#obs: essa forma é normalmene utilizada para atualizar valores de um dicionario existente 

#obs geral: onde tem dict, é para substuir pelo o dicionario (caso precise)

#GET (pegar um valor associado uma chave)
contatos={
    "jose@gmail.com":{"nome":"jose","telefone":"333-000"},
    "pedro@gmail.com":{"nome":"pedro","telefone":"333-000"}
}
#acessando o valor sem o metodo get
contatos["chave"] # se eu tento acessar uma chave que não exista dentro do dicionario, será lançada uma execeção

#acessando o valor com o get mas não indicando  um valor "default" caso a chave não seja encontrado.
contatos.get("chave")# se eu tento acessar uma chave, e ela não existe. Com o metodo get não será lançado uma exeção(ele retorna none)

#acessando o valor com o get  indicando  um valor "default" caso a chave  não seja encontrado.
contatos.get("chave",{}) #caso a chave n seja encontrada, o que será retornado é um dicionario vazio

#acessando o valor com o get  indicando  um valor "default" caso a chave  não seja encontrado. Entretando
#essa chave existe, então ele vai respeitar tudo que ja esta atribuido a ela, ou seja, ele n retorna um dicionario vazio
contatos.get("pedro@gmail.com",{})

#ITEMS (retorna uma lista de tuplas ja contendo chave e valor) # muito usado no for
contatos.items()

#KEYS ( retorna só a chaves do dicionario )
contatos.keys()

#POP ( remove uma chave do dicionario e retorna o valor que ele removeu  )
contatos.pop("pedro@gmail.com")

#tento remover um   elemento, caso ela não exista, ela retorna um valor padrão pra mim(default)
#obs: caso eu tente remover, e eu não coloque um valor padrão se não existir, será lançada uma exception
contatos.pop("pedro@gmail.com",{})
contatos.pop("chave","valor não econtrado")#retornando uma mensagem


#POPITEM ("remove os elementos da lista, de forma sequencial sem precisar passar o valor da chave")
contatos.popitem()
contatos.popitem()

#obs: caso esteja apagando o dicionario, e não existir mais chaves, será lançado uma exceção (KeyErro)

#SETDEFAULT (serve para atribuir uma nova chave e um valor para um dicionario de forma dinamica)
contatos={"nome":"guilherme","telefone":"33--223"}
contatos.setdefault("nome","pedro")# estou tentando atribuir um novo valor para nome, entretando essa chave ja existe um valor atribuido a ela.
#nesse caso, será retorna o valor existente ja associado a chave, e o novo valor que tentei atualizar não será setado a ela.

contatos.setdefault("idade",12)# agora nesse caso será bem sucedido, porque a chave não existe no dicionario, então será criado uma nova com o valor associado

#UPDATE (atualiza o nosso dicionario com o outro dicionario )
contatos={"jose@gmail.com":{"nome":"jose","telefone":"333-000"}}
## autalizando o valor da chave do sdicionario que ja existe
contatos.update({"jose@gmail.com":{"nome":"jose"}})
#obs: se a chave não existir, será criada dentro do dicionario 
contatos.update({"pedro@gmail.com":{"nome":"jose"}})


#VALUES(retorna todos os valores do dicioanrio, somente os valores)
contatos.values()


#IN ( verificar se existe determinada chave dentro de um dicionario)
contatos={
    "jose@gmail.com":{"nome":"jose","telefone":"333-000"},
    "pedro@gmail.com":{"nome":"pedro","telefone":"333-000"}
}

"jose@gmail.com" in contatos # verificando se a chave tall existe dentro do dicionario 
"idade" in contatos["pedro@gmail.com"]# estou verificando se existe a chave idade dentro de contatos na chave pedro@gmail.com ("estou delimitando", interno)

#DEL (removendo o valor(chave+valor) do dicionario , passo o objeto que quero remover)
contatos={
    "jose@gmail.com":{"nome":"jose","telefone":"333-000"},
    "pedro@gmail.com":{"nome":"pedro","telefone":"333-000"}
}

del contatos["jose@gmail.com"]["telefone"] # removendo apenas a chave o telefone da chave jose
del contatos["pedro@gmail.com"] # removendo tudo 

del contatos #apago o dicionario inteiro