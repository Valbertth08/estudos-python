#Construtores e Destrutores

#Construtor-inicializador ( é sempre executado, quando uma nova instancia da classe é criada)

#Destrutor(é sempre executado quando uma instancia(objeto)) é destruida (o python tem o coletor de lixo)-que é chamado automaticamente
#__del__(usado para executar algum tipo de comportamento, quando o objeto for destruido)


class Cachorro():
    def __init__(self,nome,cor,acordado=True): #sempre é executado no inicio(na instanciação)
        print("Incializando a classe")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado
    
    def falar(self):
        print("auau")

    def __del__(self): #sempre é executado de forma automatica no momento da destruição do objeto
        print("Removendo a instancia da classe")

def criar_cachorro():
    c=Cachorro("Zeus","Branco e preto",False)
    print(c)
    
c= Cachorro("br","preto")
c.falar()
#Forçando a destruição de um objeto
print("Ola mundo!")    
print("Ola mundo!")  
del c # para forçar a destruição de objeto, utilizamos a palavra del e o nome do objeto, assim, o obejto ele vai ser destruido em uma parte especifica da execução do programa, não somente no final
print("Ola mundo!")    
print("Ola mundo!")    
print("Ola mundo!")    
print("Ola mundo!")  