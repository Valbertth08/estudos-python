#Propriedades (normalmente utilizada para criar uma regra() de acesso para determinado atributo)
class Foo:

    def __init__(self,x= None):
        self._x=x

     #usado para retorna um valor
    @property #defino que esse metodo é uma propriedade, ou seja, ele pode ser acessado como atributo
    def x(self):
        return self._x or 0
    
    @x.setter # isso é feito para atribuir um valor para a prpriedade
    def x(self, value): # isso não é um metodo, a gente trabalha com ele como se fosse uma atributo
        self._x+=value
        
    @x.deleter # excluindo a propriedade 
    def x(self):
        self._x=0 # isso só foi um exemplo, colocando o -1

    def __str__(self) :
        return f"valor: {self.x}"
    
foo= Foo(10)
print(foo.x)
foo.x=30
print(foo.x)
del foo.x
print(foo.x)
print(foo)