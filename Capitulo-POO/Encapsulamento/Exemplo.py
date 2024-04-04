class Pessoa:
    def __init__(self,nome,ano_nascimento) -> None:
        self._nome=nome
        self.ano_nascimento=ano_nascimento

    @property
    def nome(self):
        return self._nome
    @property 
    def idade(self): # fiz um calculo pegando a data de nascimento e o ano atual
        _ano_atual=2022
        return _ano_atual- self.ano_nascimento
    
pessoa=Pessoa("pedro",2002)
print(f"nome: {pessoa.nome} \tidade: {pessoa.idade}")