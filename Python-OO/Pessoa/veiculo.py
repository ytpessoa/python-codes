

class Veiculo:
    def __init__(self, modelo:str, cor:str) -> None:
        self.__modelo = modelo #atributo privado
        self.__cor = cor #atributo privado    
    def __str__(self) -> str:
        return f"{self.__modelo} {self.__cor}"    
    @property #para ser possivel acessar o atribulto diretamente no "objeto.modelo"
    def modelo(self) -> str:
        return self.__modelo    
    @property#para ser possivel acessar o atribulto diretamente no "objeto.cor"
    def cor(self) -> str:
        return self.__cor
    @cor.setter #para poder alterar diretamente
    def cor(self, cor:str) -> None:
        self.__cor = cor

corsa = Veiculo("Fusca", "preto")