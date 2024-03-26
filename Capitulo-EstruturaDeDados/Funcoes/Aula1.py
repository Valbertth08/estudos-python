
#criando uma função 
def exibir_mensagem():
    print("olá mundo!")

def exibir_mensagem_1(nome):# sou obrigado a passar o valor para o parametro nome 
    print(f"seja bem vindo {nome}!")

def exibir_mensagem_2(nome="Anônimo"): # passando um valor default. Dessa forma é opcional passar o nome.
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_1("fabio")
exibir_mensagem_2()
exibir_mensagem_2("felipe")

#retonrando valores 
#utilizamos a palavra return (toda função retorna none por padrão)

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor=numero-1
    sucessor=numero+1

    return antecessor, sucessor# retornando dois valores em forma de tupla
calcular_total([10,20,34]) 
retorna_antecessor_e_sucessor(10)

#argumentos nomeados (chave e valor)

def calcular_total(marca,modelo,ano,placa):# eu utilizando dessa forma, posso inverter os valores na inserção na função
    return sum(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") 

#dificilmente eu iria errar os valores de inserção, porque eles são nomeados
def calcular_total(marca="fiat",modelo="palio",ano=1999,placa="ABC-1234"):
    return sum(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") 

calcular_total(**{"marca:":"Fiat","modelo":"palio","ano":1999,"placa":"ABC-1234"})# os dois asteristicos, converte os valores do dicionario, passa um dicionario pra função.

#** ( indico que ele recebe um dicionario )
#Args e Kwargs
#*args os valores vem como uma tupla ( e indico que os valores passados para o parametro dessa função vai ser uma tupla tbms)
#**kwargs, os valores vem como um dicionario (idncio que os valores passado para o argumento dessa funçõa. precisa ser um dicionario)
 
def salvar(valor, *tupla,**dicionrio):
    print("qualquer coisa: ")
