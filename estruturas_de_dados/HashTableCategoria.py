from funcoes.numeros_primos import gerar_numeros_primos

class HashTableCategoria():
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def size(self):
        return len(self.chaves)
    
    def hash(self, categoria):
        if self.fator_carga > 0.65:
            self.dobrar_tamanho()
        
        nome_categoria = categoria.getNome()
        numeros_primos = gerar_numeros_primos(len(nome_categoria))
        
        hash = int()

        for i in range(1, len(nome_categoria)):
            hash += ( ord(nome_categoria[i-1]) + 1) * numeros_primos[i-1]
        
        return hash % self.size()

    def hash_existente(self, hash):

        for i in range (hash, len(self.chaves)-1):

            if self.chaves[i] == None:
                return i
            else:
                for i in range (0, hash):
                    if self.chaves[i] == None:
                        return i
                    
                
                
          
    
    def inserir_categoria(self, categoria):
        #self.tamanho += 1
        pass

    def deletar_categoria(self, categoria):
        #self.tamanho -= 1
        pass

    def dobrar_tamanho(self):
        self.chaves += [None] * self.size()
        self.valores += [None] * self.size()

    def inserir_Categoria(self):

       pass

if __name__ == "__main__":
    pass