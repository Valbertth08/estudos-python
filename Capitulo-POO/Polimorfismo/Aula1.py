#Polimorfismo(ter muitas formas),mesmo nome de função mas assinaturas diferentes, sendo usada para tipos diferentes

#Polimorfismo com herança
#Na herança, a classe filha herda metodos da classe pai.( no ententanto, a classe filha pode modificar esse metodo)/sobrescrita


class Passaro:
    
    def voar(self):
        print("Voando..")

class Pardal( Passaro):
    def voar(self):
        print("pardal pode voar")

class Avestruz (Passaro):
    def voar(self):
     print("Avestruz não pode voar")

def plano_voo(Passaro):
        Passaro.voar()

class Aviao(Passaro): #EXEMPLO RUIM, ISSO NÃO SE FAZ.
    def voar(self):
        print("Avião esta decolando")


p1=Pardal()
p2= Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())