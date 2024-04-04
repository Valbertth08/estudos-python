
#HERANÇA MULTIPLA

class Animal:
    def  __init__(self,n_patas) :
        self.n_patas=n_patas

    def __str__(self):
        return f"{self.n_patas}"

class Mamifero(Animal):
    def  __init__(self,cor_pelo, **kw): # os atributos da classe pai, são definidas dentro desse dicionario.
       super().__init__(**kw)# dessa primeira forma todos os atributos novos que são criados no pai, também serão passados automaticamente para o filho
       self.cor_pelo=cor_pelo
      
class Ave(Animal):
     def  __init__(self,cor_bico, **kw) :# como é chave e valor, a chave numero de patas existe tanto em animal e mamifero, mas como não pode chaves repetidas
        super().__init__(**kw)
        self.cor_bico=cor_bico

class FalarMixin(): #definie simplismente um metodo para ser executado na outra classe(também é uma herança)
    def falar(self):
        return "oi estou falando"
    
class Gato(Mamifero):
     def __str__(self):
        return "gato"

class Onitorinco(Mamifero,Ave,FalarMixin): #essa é a herança multipla
      def __str__(self):
        return "onitorinco"
      
Gato= Gato(n_patas=4,cor_pelo="preto")
print(Gato)

Onitorinco= Onitorinco(n_patas=2,cor_pelo="vermelho",cor_bico="laranja") # quando é utilizado kwards, é o obrigatorio fazer os atributos nomedados, ou seja, chave e valor
print(Onitorinco)

#metodo MRO ( mostra a execução de determinado metodo, de acordo com sua ordem hieareaquica, nosso exemplo.. o metodo pego é o str)
print(Onitorinco) # se eu definir o metodo str em animal, o que será executado será o definido em animal. entretando, se eu definir em onitorinco o que será executado é no onitorinco 

print(Onitorinco.mro())# mostra  a ordem da resolução dos metodos

#MIXIN
print(Onitorinco.falar())


#No exemplo que você forneceu, a classe Animal tem um construtor __init__ que inicializa um atributo n_patas. Ambas as classes Mamifero e Ave chamam o construtor __init__ de Animal usando super().__init__(**kw). 
#O Python garante que, ao usar a herança múltipla, cada classe pai seja chamada apenas uma vez, mesmo que seja referenciada em várias partes da hierarquia de herança.
#Portanto, quando você cria uma instância de Onitorinco, que herda de Mamifero e Ave, o Python garante que o construtor __init__ de 
#Animal seja chamado apenas uma vez, evitando a duplicação de atributos. Ambas as classes Mamifero e Ave compartilham o mesmo construtor __init__ de Animal, o que impede a duplicação de inicialização de atributos.