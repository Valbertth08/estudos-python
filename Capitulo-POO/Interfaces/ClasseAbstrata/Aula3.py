from abc import ABC, abstractmethod, abstractproperty #isso é a forma pra me conseguir utilizar a anotação @abstract metode


# INTERFACES( definie o que uma classe deve fazer, e não como)- um padrão(contrato)
# o python não tem a palavra  "interface"  direta, no python são as classes abstratas.(por conta da herança multipla)
#CRIANDO CLASSES ABSTRATAS(MODULO ABC) @ABSTRACT BASE CLASS

#uma classe abstrata não pode ser instancia de forma direta partindo dela, ela precisa que suas classes filas a instancie
class Controle_Remoto(ABC):

    @abstractmethod # estou obrigando a classe que extende dessa classe abstrata, a implementar esses metodos abstratos
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty# estou indicando que todo que implementa essa classe, é obrigado a implementar essa propriedade
    def marca(self):
        pass


class ControleTv(Controle_Remoto):
    def ligar(self):
        print("Ligando a Tv")

    def desligar(self):
        print("desligando a TV")
        print("Deslgiado!")
    
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(Controle_Remoto):
    def ligar(self):
        print("Ligando o arcondicionado")

    def desligar(self):
        print("desligando o arcondionado")
        print("Deslgiado!")

    @property
    def marca(self):
        return "LG"



controle= ControleTv()
controle.ligar()
controle.desligar()

controle2= ControleArCondicionado()
controle2.ligar()
controle2.desligar()

print(controle.marca)
print(controle2.marca)