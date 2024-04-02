
#HERANÇA: é a capacidade de uma classe filha derivar ou herdar caracteristicas e comportamentos da classe pai
#fornece reutilização de código,não precisamos escrever o mesmo código reptidamente.Além disso, permite adicionar mais recursos a uma classe sem modificala.
#as modificações da classe pai, reflete diretamente na classe filha e em toda hieriarquia vindo posteriormente


#CRIAÇÃO
class A:
    def printar(self):
     print("classe A")
     
class B(A): # extend 
  def printar(self):#exemplo
     print("classe B")


class C: # extend 
  def printar(self):#exemplo
     print("classe B")

        
# HERANÇA SIMPLES E HERANÇA MULTIPLA
#HERANÇA SIMPLES(É QUANDO A CLASSE FILHA HERDA APENAS DE UMA CLASSE(base-pai    ))
     
#HERANÇA MULTIPLA(QUANDO UMA CLASSE FILHA HERDA MAIS DE UMA CLASSE(base-pai)) 
class D(A, C): # extend  (NO CASO ELA É FILHA DE A E B)
    def printar(self):#exemplo
        print("classe B")