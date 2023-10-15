from funcoes.numeros_primos import gerar_numeros_primos

class HashTableEvento():
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def size(self):
        return len(self.chaves)
    
    def hash(self, evento):
        
        nome_evento = evento.getNome()
        numeros_primos = gerar_numeros_primos(len(nome_evento))
        
        hash = int()

        for i in range(1, len(nome_evento)):
            hash += ( ord(nome_evento[i-1]) + i) * numeros_primos[i-1]
        
        return hash % self.size()
    
    def inserir_evento(self, evento):
        #self.tamanho += 1
        pass

    def remover_evento(self, categoria_evento, nome_evento):
        #self.tamanho -= 1
        pass

    def dobrar_tamanho(self):
        pass

if __name__ == "__main__":
    pass