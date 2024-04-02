#HERANÇA SIMPLES

#OS ATRIBUTOS JA SÃO DEFINIDOS AUTOMATICAMENTE NAS CLASSES FILHAS(herda o construtor)
class Veiculo:
    
    def __init__(self,cor,placa,numero_rodas):
        self.cor=cor
        self.placa=placa
        self.numero_rodas=numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas,carregado): #construtor é diferente 
        super().__init__(cor, placa, numero_rodas) 
        self.carregado=carregado 
         
    #obs, eu posso sobrescrever o metodo da classe pai, entretando se eu quiser codigo do pai, preciso utilizar a palavra super(isso no construtor)
    def esta_carregado(self): # o caminha não tem seu metodo especifico
        print(f"{'sim' if self.carregado else 'não'} estou carregado")
    
    
    def __str__(self) :
        return self.cor

moto= Motocicleta("preta","abc-123",2)
moto.ligar_motor()

carro=Carro("branco","xde-0098",4)
carro.ligar_motor()

Caminhao=Caminhao("roxo","gft-8712",8,True)
Caminhao.esta_carregado()
print(Caminhao)