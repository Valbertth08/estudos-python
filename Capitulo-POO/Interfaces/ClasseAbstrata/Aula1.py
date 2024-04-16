#VARIAVES DE CLASSES VARIAVES DE INSTANCIA

#Atributos de instancia: São diferentes para cada objeto(objeto tem uma copia dos atributos)
#Atributos de classe: São compartilhados entre os objetos(pertence a classe)

class Estudante:
    escola="Dio"
    def  __init__(self,nome,matricula):
        self.nome=nome
        self.matricula=matricula

    def __str__(self) -> str:
        return f"{self.nome}- {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1=Estudante("val",1)
aluno2=Estudante("valb",2) 

mostrar_valores(aluno1,aluno2)
Estudante.escola="Python"
aluno2.matricula=3
mostrar_valores(aluno1,aluno2)