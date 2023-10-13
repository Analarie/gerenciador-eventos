class Evento:
    def __init__(self, nome, categoria, descricao):
        self.nome = nome
        self. categoria = categoria
        self.descricao = descricao
    
    def getNome(self):
        return self.nome
    
    def getCategoria(self):
        return self.categoria