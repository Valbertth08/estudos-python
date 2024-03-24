#criação de um dicionario

pessoa={"nome":"guilherme","idade":28}
pessoa=dict(nome="guilherme",idade=28)#utilizando a classe dict
pessoa["telefone"]="3333-1234" # estou adicionando uma nova chave no meu dicionario existente

#acessando ao dados 
pessoa={"nome":"guilherme","idade":28}
pessoa["nome"] #estou acessando ao valor a chave nome

#sobrescrevendo o valor
pessoa={"nome":"guilherme","idade":28}
pessoa["nome"]="joão"


#dicionarios aninhados(um dicionario dentro do outro)

contatos={
    "jose@gmail.com":{"nome":"jose","telefone":"333-000"},#tenho um dicionario geral, e outro dicionario associado a uma chave do dicionario geral
    "pedro@gmail.com":{"nome":"pedro","telefone":"333-000"}
}
contatos["jose@gmail.com"]["telefone"]=1234# estou atualizando a chave especifica do meu outro dicionario 
#obs: isso seja pra acessar, ou atualizar.

#iterar sobre um dicionario

#1 forma(não é muito recomendada)
for chave in contatos:
    print(chave,contatos[chave])

#2 forma
for chave,valor in contatos.items():
    print(chave,valor)
#o items() retorna uma lista de tuplas, onde o primeiro valor é a chave, e o segundo é o valor

