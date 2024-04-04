#Conceito Protação de dados de uma classe (restrições a acesso a variaveis e metodos)


#Modificadores de Acesso

#O python não tem palavras reservadas, ela só tem convenções ( fica a criterio do programador)

#Modificador publico: Pode ser acessado fora da classe
#Privado: Só pode ser acessado pela classe e não pode ser acessados diramente fora da classe, ou seja, escrito ou lido.

#Para indicar que uma variavel ou metodo é privado, é convencional que coloque o _(underline) na frente de ambos,
#entretanto, isso é só uma convenção, tudo ainda continua publico



#Ex:
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo=saldo
        self.nro_agencia= nro_agencia


    def depositar (self,valor):
        self._saldo+=valor

    def sacar(self,valor):
        self._saldo-=valor
    
    def mostrar_saldo(self): # utilizo os metodos para acessar a uma variavel privada 
        return self._saldo


conta= Conta("0001",100)
print(conta._saldo)# estou acessando a variavel mesmo eu indicando por convenção que é privada.
print(conta.nro_agencia)
print(conta.mostrar_saldo())

