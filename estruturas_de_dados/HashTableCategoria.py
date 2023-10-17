from funcoes.numeros_primos import primo_antecessor, primo_sucessor, gerar_numeros_primos
from estruturas_de_dados.HashTableEvento import HashTableEvento
from classes.Categoria import Categoria

class Tipo(type):
    def __repr__(self):
        return self.__name__

class HashTableCategoria(metaclass = Tipo):
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def atualiza_fator_carga(self):
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
            self.atualiza_fator_carga()
        else:
            if self.chaves[indice_insercao] != categoria.getNome():
                
                indice_auxiliar = indice_insercao + 1
                while True:
                    if self.chaves[indice_auxiliar] == None:
                        hash_table_para_eventos = HashTableEvento()

                        self.chaves[indice_auxiliar] = categoria.getNome()
                        self.valores[indice_auxiliar] = hash_table_para_eventos
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    elif self.chaves[indice_auxiliar-2] == None:
                        hash_table_para_eventos = HashTableEvento()

                        self.chaves[indice_auxiliar-2] = categoria.getNome()
                        self.valores[indice_auxiliar-2] = hash_table_para_eventos
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    else:
                        if indice_auxiliar + 1 >= self.size():
                            indice_auxiliar = 0
                        else:
                            indice_auxiliar += 1

    def get_eventos_categoria(self, nome_categoria):
        """
        Retorna o valor (hash table de eventos) de uma categoria caso ela esteja armazenada.
        
        Caso a categoria não exista na tabela, retorna False.
        """
        
        indice_insercao = self.hash(Categoria(nome_categoria))

        if self.chaves[indice_insercao] == None:
            return False
        elif self.chaves[indice_insercao] == nome_categoria:
            return self.valores[indice_insercao]
        else:
            if indice_insercao >= len(self.chaves)//2:
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        return self.valores[indice_insercao]
                    
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        return self.valores[indice_insercao]
            else:
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        return self.valores[indice_insercao]
                
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        return self.valores[indice_insercao]

        return False

    def listar_categorias(self):
        """
        Retorna uma string com o nome de todas as categorias armazenadas na HashTable.

        Retorna "Nenhuma categoria armazenada." caso não existam categorias na tabela.
        """

        if self.tamanho == 0:
            return "Nenhuma categoria armazenada."
        
        categorias_armazendas = "Categorias armazendas: "
        for categoria in self.chaves:
            if categoria != None:
                categorias_armazendas += categoria
                categorias_armazendas += ", "
        
        return categorias_armazendas[:-2]
    
    def existe_categoria(self, nome_categoria):
        """
        Retorna True caso a categoria exista na HashTable, e False caso não.
        """

        indice_insercao = self.hash(Categoria(nome_categoria))

        if self.chaves[indice_insercao] == None:
            return False
        elif self.chaves[indice_insercao] == nome_categoria:
            return True
        else:
            if indice_insercao >= len(self.chaves)//2:
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        return True
                    
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        return True
            else:
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        return True
                    
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        return True
        return False
    
    def remover_categoria(self, nome_categoria):
        """
        Dado um nome de categoria, remove a categoria da HashTable caso ela esteja armazenada e retorna seu nome.
        """

        categoria_removida = False

        indice_insercao = self.hash(Categoria(nome_categoria))

        if self.chaves[indice_insercao] == None:
            print("A categoria informada não existe na tabela hash.")
            categoria_removida = True
        
        elif self.chaves[indice_insercao] == nome_categoria:
            self.chaves[indice_insercao] = None
            self.valores[indice_insercao] = None
            self.tamanho -= 1
            self.atualiza_fator_carga()
            return nome_categoria
        
        else:
            if indice_insercao >= len(self.chaves)//2:
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_categoria
                    
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_categoria
                    
            else:
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_categoria:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_categoria
                
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_categoria:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_categoria
        
        if not categoria_removida:
            print("A categoria informada não existe na tabela hash.")

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
                                
        self.atualiza_fator_carga()

if __name__ == "__main__":
    pass