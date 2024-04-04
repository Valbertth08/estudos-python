
class veiculo:
    def __init__(self,nr_rodas,cor,teste):
        self.nr_rodas=nr_rodas
        self.cor=cor
        self.teste=teste


class andar: # só uma classe, com um metodo, e adiciono ela em uma classe filha, sem ter nenhum acoplamento aauto
    def mover(self):
     return "andando"
    
    
class moto(veiculo,andar):
    def __init__(self, marca,**kw):# isso indico os atributos da classe pai 
        super().__init__(**kw) # fica dinamico, se tiver novos atributos no pai, ja sera repassado para o filho

        self.marca=marca

    def __str__(self):
        return f"marca: {self.marca} numero de rodas: {self.nr_rodas} cor: {self.cor} teste: {self.teste}"


moto = moto(nr_rodas=2, teste="teste", cor="vemelho",marca="honda") # na herança multipla ou herança, o construtor é compartilhado

print(moto.mover())


#Você está correto, me desculpe pelo equívoco. Vamos revisar a questão da herança múltipla e o método __init__ na classe Onitorinco considerando que a classe Ave também possui um método __init__.

#No Python, quando uma classe possui um método __init__ e você chama super().__init__(**kw) dentro desse método, o método __init__ da primeira superclasse válida (de acordo com a ordem de herança) que tiver o método __init__ é chamado. Se a primeira superclasse não tiver o método __init__, o Python procurará na próxima superclasse e assim por diante.

#Então, no caso do Onitorinco que herda de Mamifero, Ave, e FalarMixin, o método __init__ de Mamifero é chamado primeiro, que por sua vez chama o método __init__ de Animal através de super().__init__(**kw). Depois, o método __init__ de Ave não é chamado novamente porque a classe Ave é a última na ordem de herança, e o Python evita chamar construtores de classes já chamadas na resolução de MRO.

#Portanto, o Onitorinco teria o atributo n_patas definido pela classe Animal através da herança de Mamifero, e não haveria duplicação desse atributo.

#O Python garante que, ao usar a herança múltipla, cada classe pai seja chamada apenas uma vez, mesmo que seja referenciada em várias partes da hierarquia de herança.
#Portanto, quando você cria uma instância de Onitorinco, que herda de Mamifero e Ave, o Python garante que o construtor __init__ de 
#Animal seja chamado apenas uma vez, evitando a duplicação de atributos. Ambas as classes Mamifero e Ave compartilham o mesmo construtor __init__ de Animal, o que impede a duplicação de inicialização de atributos.


