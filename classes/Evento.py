class Evento:
    def __init__(self, evento, descricacao, categoria):
        self.nome = evento
        self.categoria = categoria
        self.descricao = descricacao
    
    def getNome(self):
        return self.nome
    
    def getCategoria(self):
        return self.categoria
    
    def getDescricao(self):
        return self.descricao


if __name__ == "__main__":
    pass