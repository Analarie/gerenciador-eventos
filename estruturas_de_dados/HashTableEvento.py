from funcoes.numeros_primos import primo_antecessor, primo_sucessor, gerar_numeros_primos
from classes.Evento import Evento

class Tipo(type):
    def __repr__(self):
        return self.__name__

class HashTableEvento(metaclass = Tipo):
    
    def __init__(self, tamanho_inicial=11):
        self.chaves = [None] * tamanho_inicial
        self.valores = [None] * tamanho_inicial

        self.tamanho = 0
        self.fator_carga = self.tamanho / self.size()
    
    def atualiza_fator_carga(self):
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

            for i in range(1, len(nome_evento)):
                hash += ( ord(nome_evento[i-1]) + i) * numeros_primos[i-1]

            return hash % self.size()

    def inserir_evento(self, evento):
        """
        Dada uma instância de Evento insere o nome do evento como chave da hash table e a instância de Evento como valor, caso o evento não exista na hash table.
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
                        self.valores[indice_auxiliar] = evento
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    elif self.chaves[indice_auxiliar-2] == None:

                        self.chaves[indice_auxiliar-2] = evento.getNome()
                        self.valores[indice_auxiliar-2] = evento
                        self.tamanho += 1
                        self.atualiza_fator_carga()
                        break

                    else:
                        if indice_auxiliar + 1 >= self.size():
                            indice_auxiliar = 0
                        else:
                            indice_auxiliar += 1

    def existe_evento(self, nome_evento):
            """
            Retorna True caso o evento exista na HashTable, e False caso não.
            """

            indice_insercao = self.hash(Evento(nome_evento, "", ""))

            if self.chaves[indice_insercao] == None:
                return False
            elif self.chaves[indice_insercao] == nome_evento:
                return True
            else:
                if indice_insercao >= len(self.chaves)//2:
                    for i in range(indice_insercao + 1, len(self.chaves)):
                        if self.chaves[i] == nome_evento:
                            return True
                        
                    for i in range(indice_insercao):
                        if self.chaves[i] == nome_evento:
                            return True
                else:
                    for i in range(indice_insercao):
                        if self.chaves[i] == nome_evento:
                            return True
                        
                    for i in range(indice_insercao + 1, len(self.chaves)):
                        if self.chaves[i] == nome_evento:
                            return True
            return False

    def remover_evento(self, nome_evento):
        """
        Dado um nome de evento, remove o evento da HashTable caso ele esteja armazenado e retorna seu nome.
        """

        evento_removido = False

        indice_insercao = self.hash(Evento(nome_evento, "", ""))

        if self.chaves[indice_insercao] == None:
            print()
            print(f"O evento '{nome_evento}' não existe na tabela hash.")
            
            evento_removido = True
        
        elif self.chaves[indice_insercao] == nome_evento:
            self.chaves[indice_insercao] = None
            self.valores[indice_insercao] = None
            self.tamanho -= 1
            self.atualiza_fator_carga()
            return nome_evento
        
        else:
            if indice_insercao >= len(self.chaves)//2:
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_evento:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_evento
                    
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_evento:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_evento
                    
            else:
                for i in range(indice_insercao):
                    if self.chaves[i] == nome_evento:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_evento
                
                for i in range(indice_insercao + 1, len(self.chaves)):
                    if self.chaves[i] == nome_evento:
                        self.chaves[i] = None
                        self.valores[i] = None
                        self.tamanho -= 1
                        self.atualiza_fator_carga()
                        return nome_evento
        
        if not evento_removido:
            print(f"O evento '{nome_evento}' não existe na tabela hash.")

    def listar_eventos(self):
        """
        Retorna uma string coom o nome de todos os eventos armazenadas na HashTable.
        
        Retorna "Nenhum evento armazenado." caso não existam eventos na tabela.
        """

        if self.tamanho == 0:
            return "Nenhum evento armazenado."

        eventos_armazenados = "Eventos armazenados: "
        for evento in self.chaves:
            if evento != None:
                eventos_armazenados += evento
                eventos_armazenados += ", "
        
        return eventos_armazenados[:-2]

    def imprimir_dados_eventos(self):
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

                evento = Evento(temp_chaves[i], "", "")
                indice_insercao = self.hash(evento)

                if self.chaves[indice_insercao] == None:

                    self.chaves[indice_insercao] = evento.getNome()
                    self.valores[indice_insercao] = temp_valores[i]
                    self.tamanho += 1
                else:   
                    indice_auxiliar = indice_insercao + 1
                    while True:
                        if self.chaves[indice_auxiliar] == None:

                            self.chaves[indice_auxiliar] = evento.getNome()
                            self.valores[indice_auxiliar] = temp_valores[i]
                            self.tamanho += 1
                            break

                        elif self.chaves[indice_auxiliar-2] == None:

                            self.chaves[indice_auxiliar-2] = evento.getNome()
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