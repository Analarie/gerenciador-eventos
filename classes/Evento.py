class Tipo(type):
    def __repr__(self):
        return self.__name__

class Evento(metaclass = Tipo):
    def __init__(self, nome, categoria, descricao):
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
    
    def getNome(self):
        return self.nome
    
    def getCategoria(self):
        return self.categoria

    def getDescricao(self):
        return self.descricao

if __name__ == "__main__":
    pass