#Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as 
#opções de destino e imprimir a selecionada)

class Viajante:
    def __init__(self, nome):
        self.nome=nome

def cadastrar(viajante):
    nome=input("Informe o nome do viajante: ")
    viajante.nome=nome
    lista=["são luis","São pedro","Fernando de noronha"]
    for p, i in enumerate(lista):
        print(f"{p+1} Viagem: {i}")
    valor=int(input("Informe o a viagem desejada: "))
    print(f"Boa viagem {viajante.nome} Viagem para: "+lista[valor-1])
viajante= Viajante("Pedro")
cadastrar(viajante)




