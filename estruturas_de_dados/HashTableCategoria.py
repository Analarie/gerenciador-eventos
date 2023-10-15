from funcoes.numeros_primos import primo_antecessor, primo_sucessor, gerar_numeros_primos
from estruturas_de_dados.HashTableEvento import HashTableEvento
from classes.Categoria import Categoria

class HashTableCategoria():
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def size(self):
        return len(self.chaves)
    
    def hash(self, categoria):
        """
        Dada uma instância da classe Categoria, retorna um valor hash.
        """

        nome_categoria = categoria.getNome()
        numeros_primos = gerar_numeros_primos(len(nome_categoria))
        
        hash = int()

        for i in range(1, len(nome_categoria)):
            hash += ( ord(nome_categoria[i-1]) + i) * numeros_primos[i-1]

        return hash % self.size()

    def inserir_categoria(self, categoria):
        """
        Insere nome da categoria como chave e uma HashTableEvento como valor em uma instância de HashTableCategoria, caso a categoria não exista na hash table.
        """

        if self.fator_carga >= 0.7 and self.fator_carga <= 0.8:
            self.dobrar_tamanho()
        
        indice_insercao = self.hash(categoria)
        
        if self.chaves[indice_insercao] == None:
            hash_table_para_eventos = HashTableEvento()

            self.chaves[indice_insercao] = categoria.getNome()
            self.valores[indice_insercao] = hash_table_para_eventos
            self.tamanho += 1
        else:
            if self.chaves[indice_insercao] != categoria.getNome():
                
                indice_auxiliar = indice_insercao + 1
                while True:
                    if self.chaves[indice_auxiliar] == None:
                        hash_table_para_eventos = HashTableEvento()

                        self.chaves[indice_auxiliar] = categoria.getNome()
                        self.valores[indice_auxiliar] = hash_table_para_eventos
                        self.tamanho += 1
                        break

                    elif self.chaves[indice_auxiliar-2] == None:
                        hash_table_para_eventos = HashTableEvento()

                        self.chaves[indice_auxiliar-2] = categoria.getNome()
                        self.valores[indice_auxiliar-2] = hash_table_para_eventos
                        self.tamanho += 1
                        break

                    else:
                        if indice_auxiliar + 1 >= self.size():
                            indice_auxiliar = 0
                        else:
                            indice_auxiliar += 1

    def get_valor_categoria(self, categoria):
        if self.existe_categoria(categoria):
            pass

    def existe_categoria(self, categoria):
        pass

    def remover_categoria(self, nome_categoria):
        #self.tamanho -= 1
        pass

    def dobrar_tamanho(self):
        """
        Redimensiona a capacidade da HashTable para o número primo mais próximo ao dobro de sua capacidade atual.

        Insere novamente as chaves e valores na HashTable utilizando a função hash() de acordo com a nova capacidade da HashTable.
        """

        temp_chaves = self.chaves
        temp_valores = self.valores

        primoSucessor = primo_sucessor( self.size()*2 )
        primoAntecessor = primo_antecessor( self.size()*2 )

        if int(self.size()*2 - primoAntecessor) <= int(primoSucessor - self.size()*2):
            self.chaves = [None] * primoAntecessor
            self.valores = [None] * primoAntecessor
            self.tamanho = 0
        else:
            self.chaves = [None] * primoSucessor
            self.valores = [None] * primoSucessor
            self.tamanho = 0
        
        for i in range( len(temp_chaves) ):
            if temp_chaves[i] != None:

                categoria = Categoria(temp_chaves[i])
                indice_insercao = self.hash(categoria)

                if self.chaves[indice_insercao] == None:

                    self.chaves[indice_insercao] = categoria.getNome()
                    self.valores[indice_insercao] = temp_valores[i]
                    self.tamanho += 1
                else:   
                    indice_auxiliar = indice_insercao + 1
                    while True:
                        if self.chaves[indice_auxiliar] == None:

                            self.chaves[indice_auxiliar] = categoria.getNome()
                            self.valores[indice_auxiliar] = temp_valores[i]
                            self.tamanho += 1
                            break

                        elif self.chaves[indice_auxiliar-2] == None:

                            self.chaves[indice_auxiliar-2] = categoria.getNome()
                            self.valores[indice_auxiliar-2] = temp_valores[i]
                            self.tamanho += 1
                            break

                        else:
                            if indice_auxiliar + 1 >= self.size():
                                indice_auxiliar = 0
                            else:
                                indice_auxiliar += 1

if __name__ == "__main__":
    pass