class Tipo(type):
    def __repr__(self):
        return self.__name__

class Categoria(metaclass = Tipo):
    def __init__(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

if __name__ == "__main__":
    pass