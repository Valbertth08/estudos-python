#Parametros especiais (por posição,posição e nome, ou por nome)

#"/"(position only) obrigo a passar o parametro, sem ser nomeado 
#obs: são obrigatorios ser por posição todos o valores  antes da barra, os depois da barra, pode ser nomeado ou só por posição
#ex:
def teste (modelo,carro,/,marca,outo):
    print("qualquer coisa")

def teste (modelo,carro,/,marca="tall", outo="tall"):
    print("qualquer coisa")

#"*" só parametros nomeados(essa função só aceita parametros nomeados)
def teste (*,modelo="palio",carro="fiat",marca="tall", outo="tall"):
 print("qualquer coisa")  

#"*","/"(hibidro)position only and keyword()
def teste (modelo,carro,/,*,marca="tall", outo="tall"):
    print("qualquer coisa")


#OBJETOS DE PRIMEIRA CLASSE ( FUNÇÕES PODEM SER PASSADAS COMO ARGUMENTOS PARA OUTRAS FUNÇÕES/ATRIBUIR PARA UMA FUNÇÃO E RETORNA-LA DE UM METODO)
    
def somar(a,b):
   return a+b

def subtrair(a,b):
   
   return a-b
def exibir_resultado(a,b, funcao):
   resultado=funcao(a,b)
   print(f"o resultado da operação é = {resultado}")

exibir_resultado(10,10,somar)#obs, eu não executo ela, eu passo a função como referencia
exibir_resultado(10,10,subtrair)

#fazendo apontamento para uma função, atraves de uma variavel

#ex
op= somar  #indico que a variavel recebe a função e eu executo a função com o nome da variavel agora
print(op(5,10))


#Escopo local e global

#escopo local= tudo que é feito dentro de um escopo especifico
#escopo global= informa para o interpretador que a varaivel que esta sendo usada no escopo local é global( essa não é uma boa pratica)

salario=2000 #variavel definida fora da função

def salario_bonus(bonus,lista):

   lista.append(2)
   global salario# informo que a variavel esta fora do escopo local, e esta no global
   salario+=bonus # a variavel esta fora do meu escopo local 
   return salario


lista=[1]
print(salario_bonus(500,lista))
print(lista) # foi incrementado na lista, porque a lista é um objeto imutavel( por referencia )