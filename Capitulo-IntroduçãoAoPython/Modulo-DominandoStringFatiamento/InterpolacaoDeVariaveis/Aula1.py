
#utilzando porcetagem %
nome="guilherme"
idade= 28
profissao="programdaor"

print("nome %s, idade %d, profissoa %s" %(nome,idade,profissao))# substitui tudo pelo as variaveis indicadas

#utilizando o format
nome="guilherme"
idade= 28
profissao="programdaor"

dados={"nome":nome,"idade":idade,"profissao":profissao}
print("nome {}, idade {}, profissoa {}".format(nome,idade,profissao))# substituo na sequencia
print("nome {1}, idade {0}, profissoa {1} nome dnv {1}".format(nome,idade,profissao))#indico atraves do numero da sequencia onde cada variavel vai(posição)
print("nome {nome}, idade {idade}, profissoa {profissao} nome dnv {nome}".format(nome="pedro",idade=20,profissao="programador"))# indico atraves do nome onde cada string vai entrar
print("nome {nome}, idade {idade}, profissoa {profissao} nome dnv {nome}".format(**dados))# pegando os valores do dicionario    W
#OBS: essas variaveis podem ser aproveitada em varios momentos na mesa string 

#utilizando o F-string
nome="guilherme"
idade= 28
profissao="programdaor"
print(f"nome {nome}, idade {idade}, profissoa {profissao}")# passo entre chaves o nome da variavel  

#formatação f-string
PI= 3.14159
print(f"valor de PI: {PI:.2f}")#vai ter dois numeros pos a virgula e nenhm espaço entre a a string e a concatenação
print(f"valor de PI: {PI:10.2f}")#vai ter dois numeros pos a virgula e 10 espaços("width") entre a a string e a concatenação