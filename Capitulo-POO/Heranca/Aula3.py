
#HERANÇA MULTIPLA

class Animal:
    def  __init__(self,n_patas) :
        self.n_patas=n_patas

    def __str__(self):
        return f"{self.n_patas}"

class Mamifero(Animal):
    def  __init__(self,cor_pelo, **kw):
       super().__init__(**kw)
       self.cor_pelo=cor_pelo
      
class Ave(Animal):
     def  __init__(self,cor_bico, **kw) :
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

Onitorinco= Onitorinco(n_patas=2,cor_pelo="vermelho",cor_bico="laranja")
print(Onitorinco)

#metodo MRO ( mostra a execução de determinado metodo, de acordo com sua ordem hieareaquica, nosso exemplo.. o metodo pego é o str)
print(Onitorinco) # se eu definir o metodo str em animal, o que será executado será o definido em animal. entretando, se eu definir em onitorinco o que será executado é no onitorinco 

print(Onitorinco.mro())# mostra  a ordem da resolução dos metodos

#MIXIN
print(Onitorinco.falar())

