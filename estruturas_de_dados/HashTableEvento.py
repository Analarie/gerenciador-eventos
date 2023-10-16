from funcoes.numeros_primos import gerar_numeros_primos

class Evento():
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
     
    def size(self):
        return len(self.chaves)
    
    def hash(self, eventos):
        if self.fator_carga > 0.65:
            self.dobrar_tamanho()
        
        nome_evento = Evento.getNome()
        numeros_primos = gerar_numeros_primos(len(nome_evento))
        
        hash = int()

        for i in range(1, len(nome_evento)):
            hash += ( ord(nome_evento[i-1]) + 1) * numeros_primos[i-1]
        
        return hash % self.size()
    
  
    def existe_categoria(self, categoria):
        pass

    def hash_existente(self, hash):

        for i in range (hash, len(self.chaves)-1):

            if self.chaves[i] == None:
                return i
            else:
                for i in range (0, hash):
                    if self.chaves[i] == None:
                        return i
                    
                
     


    def deletar_Evento(self, evento):
        #self.tamanho -= 1
        pass

    def dobrar_tamanho(self):
        self.chaves += [None] * self.size()
        self.valores += [None] * self.size()

    def inserir_evento(self, evento, valor):
        pass
if __name__ == "__main__":
    pass