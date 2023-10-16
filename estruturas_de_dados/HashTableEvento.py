from funcoes.numeros_primos import primo_antecessor, primo_sucessor, gerar_numeros_primos
from classes.Evento import Evento

class Evento():
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def atualiza_fator_carga(self):
        self.fator_carga = self.tamanho / self.size()    

        self.fator_carga = self.tamanho / self.size()
     
    def size(self):
        return len(self.chaves)
    
    def hash(self, evento):
            """
            Dada uma instância da classe Evento, retorna um valor hash.
            """

            nome_evento = evento.getNome()
            numeros_primos = gerar_numeros_primos(len(nome_evento))
            
            hash = int()
    def hash(self, eventos):
        if self.fator_carga > 0.65:
            self.dobrar_tamanho()
        
        nome_evento = Evento.getNome()
        numeros_primos = gerar_numeros_primos(len(nome_evento))
        
        hash = int()

        for i in range(1, len(nome_evento)):
                hash += ( ord(nome_evento[i-1]) + i) * numeros_primos[i-1]

        return hash % self.size()

    def inserir_evento(self, evento):
        """
        Insere nome da categoria como chave e uma HashTableEvento como valor em uma instância de HashTableCategoria, caso a categoria não exista na hash table.
        """

        if self.fator_carga >= 0.7 and self.fator_carga <= 0.8:
            self.dobrar_tamanho()
        
        indice_insercao = self.hash(evento)
        
        if self.chaves[indice_insercao] == None:

            self.chaves[indice_insercao] = evento.getNome()
            self.valores[indice_insercao] = evento
            self.tamanho += 1
            self.atualiza_fator_carga()
        else:
            if self.chaves[indice_insercao] != evento.getNome():
                
                indice_auxiliar = indice_insercao + 1
                while True:
                    if self.chaves[indice_auxiliar] == None:
                        

                        self.chaves[indice_auxiliar] = evento.getNome()
                        self.valores[indice_auxiliar] = hash_table_para_eventos
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    elif self.chaves[indice_auxiliar-2] == None:
                        hash_table_para_eventos = hash_table_para_eventos

                        self.chaves[indice_auxiliar-2] = evento.getNome()
                        self.valores[indice_auxiliar-2] = hash_table_para_eventos
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    else:
                        if indice_auxiliar + 1 >= self.size():
                            indice_auxiliar = 0
                        else:
                            indice_auxiliar += 1
        for i in range(1, len(self.chaves)):
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