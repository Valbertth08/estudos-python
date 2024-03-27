

#O self, é uma referencia para o objeto, explicita(instancia atual)
class Bicicleta:
    def __init__(self,cor,modelo,ano,valor): #construtor da classe
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor

    def buzinar(self): #metodos, são funções dentro de uma classe
        return "Plim plim "
    
    def parar(self): # o self é só por conversação mesmo(referencia explicita para o objeto )
        return "Parando a bicicleta...."
    
    def correr(self):
        return "Bicicleta ta correndo"
    
    def getCor(self):
        return self.cor
    
    def trocar_marchar(nro_marcha): #dessa forma, quem sera representado o "self(instancia do objeto atual)"  é o nmr_marchar, se por acaso eu não colocar  o self 
        print("Marchar alterada ")

    def __str__(self): #corresponde ao tostring do java, que é usado para mostrar de forma mais legivel o objeto
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"        

    #existe outra forma mais dinamica


caloi= Bicicleta("vermelha","caloi",2022,600)
print(caloi.buzinar())

print( caloi.cor,caloi.modelo) # acessando os atributos 
print(caloi.getCor())


#Exibindo a instancia
print(caloi)