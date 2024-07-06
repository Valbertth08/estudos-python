
class Veiculo:

    def __init__(self,marca=None,modelo=None):
        self._marca=marca
        self._modelo=modelo

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo
        
    def ligar(self):
        return f"Marca: {self._marca} Modelo: {self.modelo} , o carro esta ligando." 

class Carro(Veiculo):

    def __init__(self,num_portas,**prop):
        super().__init__(**prop)
        self._num_portas=num_portas

    @property
    def num_portas(self):
        return self._num_portas

    def  imprime_mensagem(self):
        return f"Marca: {self._marca} Modelo: {self.modelo} Numero de Portas: {self.num_portas}" 
    
carro= Carro(num_portas=4,marca="Celta",modelo="Civic")
print(carro.imprime_mensagem())
