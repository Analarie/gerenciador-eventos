class HashTableCategoria():
    
    def __init__(self, tamanho_inicial=10):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def size(self):
        return len(self.chaves)
    
    def hash(self, evento):
        pass
    
    def inserir_evento(self, evento):
        pass

    def deletar_evento(self, evento):
        pass