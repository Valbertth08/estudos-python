#METODOS ESTATICOS E METODOS DE CLASSE

#METODOS DE CLASSE =são metodos ligados a classe(recebem um parametro que aponta para a classe)-pode acessar e moficar o estado classe
#É mais utilizado para criar metodos de fabrica

#METODOS ESTÁTICOS= Não recebe um primeiro argumento explicito, também esta ligado a classe( não acessa ou modifica o estado classe)
#É mais utilizado para criar funções utilitarias

class Pessoa:

    def __init__(self,nome=None,idade=None):
        self.nome=nome
        self.idade=idade

    @classmethod #notação para indicar que é um metodo de classe
    def criar_apartir_data_nascimento(cls,ano,mes,dia,nome): # cls é uma convensão para metodos de classe
        idade=2024-ano
        return cls(nome,idade) # não preciso repetir, pessoa para criar o objeto, porque o cls é a propria classe pessoa(referencia de classe)

    @staticmethod  # indico metodo estatico (não preciso do contexto da classe e nem do metodo estatico)
    def e_maior_de_idade(idade):
        return idade>=18
    
pe=Pessoa.criar_apartir_data_nascimento(1992,3,21,"Pedro")
print(pe.nome, pe.idade)

print(Pessoa.e_maior_de_idade(18))


#Diferança

""" As duas notações @classmethod e @staticmethod são usadas para definir métodos que não dependem de uma instância específica da classe (self), mas têm propósitos ligeiramente diferentes:
@classmethod: Este decorador é usado para definir métodos de classe. Métodos de classe recebem a classe como primeiro argumento, por convenção chamado de cls. Eles podem ser chamados na própria classe, 
em instâncias da classe ou em subclasses. Métodos de classe são úteis quando você precisa criar instâncias da classe de uma maneira alternativa, como no exemplo que você deu, onde um método de classe criar_apartir_data_nascimento é usado para criar uma instância da classe Pessoa a partir da data de nascimento.
@staticmethod: Este decorador é usado para definir métodos estáticos. Métodos estáticos não recebem implicitamente uma referência à classe ou à instância (não recebem cls ou self como primeiro argumento). Eles são chamados diretamente na classe e não têm acesso a dados específicos de instância ou de classe, a menos que sejam explicitamente passados como argumentos. 
No seu exemplo, o método estático e_maior_de_idade verifica se uma idade é maior ou igual a 18, sem depender de nenhum outro atributo ou método da classe Pessoa.
Resumindo, a diferença fundamental entre @classmethod e @staticmethod é que @classmethod recebe a classe como primeiro argumento, permitindo operações que envolvam a própria classe, enquanto @staticmethod não recebe a classe ou instância automaticamente, sendo utilizado para métodos que não dependem de acesso a atributos ou métodos da classe. """