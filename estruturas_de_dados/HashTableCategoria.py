class HashTableCategoria():
    
    def __init__(self, tamanho_inicial=10):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def size(self):
        return len(self.chaves)
    
    def hash(self, categoria):
        if self.fator_carga > 0.65:
            self.dobrar_tamanho()
        
        pass

    def existe_categoria(self, categoria):
        pass
    
    def inserir_categoria(self, categoria):
        #self.tamanho += 1
        pass

    def deletar_categoria(self, categoria):
        #self.tamanho -= 1
        pass

    def dobrar_tamanho(self):
        self.chaves += [None] * self.size()
        self.valores += [None] * self.size()

if __name__ == "__main__":
    pass