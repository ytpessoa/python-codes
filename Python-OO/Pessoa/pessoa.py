class Pessoa:
    ativo = False #variavel da classe, não um atributo
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome #atributo
        self.idade = idade #atributo    
    
    #permite examinar a instancia
    def __repr__(self) -> str:
        return f"nome: {self.nome}, idade: {self.idade}, ativo: {self.ativo}"

    #permite examinar a instancia mais legivel para seres humanos
    def __str__(self) -> str:
        idade = "anos" if self.idade > 1 else "ano"
        ativo = "ativo" if self.ativo else "inativo"
        return f"{self.nome}, {self.idade} {idade} ({ativo})" 

#herança
class Pessoav2(Pessoa):
    def __init__(self, nome:str, idade:int, ativo:bool=False) -> None:
        Pessoa.__init__(self, nome, idade) #chama init classe pai: nome e idade
        self.ativo = ativo
        

pessoa = Pessoa("Ytallo", 20)
pessoa.__dict__      
#{'nome': 'Ytallo', 'idade': 20}
pessoa.ativo=True
pessoa.__dict__
#{'nome': 'Ytallo', 'idade': 29, 'ativo': True}
pessoa
#nome: Ytallo, idade: 29, ativo: False

dir(pessoa)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 'ativo', 'idade', 'nome']

