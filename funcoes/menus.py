def limpar_console():

    from os import system
    system("cls")

def mensagem_menu_inicial():

    print("======== GERENCIADOR DE EVENTOS ========")
    print("|                                      |")
    print("| 1 - INSERIR EVENTO                   |")
    print("| 2 - REMOVER EVENTO                   |")
    print("| 3 - BUSCAR EVENTO POR CATEGORIA      |")
    print("| 4 - LISTAR TODAS AS CATEGORIAS       |")
    print("| 5 - SAIR                             |")
    print("|                                      |")
    print("========================================")
    print()

def mensagem_menu_retorno():
    print()
    print("1 - VOLTAR AO MENU")
    print("2 - SAIR")
    print()

def mensagem_programa_encerrado():
    print()
    print("PROGRAMA ENCERRADO!")
    
def menu_retorno():
    mensagem_menu_retorno()

    while True:
        try:
            escolha = int(input("> "))

        except ValueError:
            print("Opção inválida, escolha 1 ou 2!")
            print()

        else:
            match (escolha):
                case 1:
                    limpar_console()
                    return True
                case 2:
                    return False
                case _:
                    print("Opção inválida, escolha 1 ou 2!")
                    print()

def menu_inicial():

    mensagem_menu_inicial()
    while True:
        try:
            escolha = int(input("> "))
            
        except ValueError:
            limpar_console()
            mensagem_menu_inicial()
            print("Opção inválida, digite um número entre 1 e 5!")
            print()

        else:
            match (escolha):
                case 1:
                    return "inserir_evento"
                case 2:
                    return "remover_evento"
                case 3:
                    return "buscar_evento"
                case 4:
                    return "listar_categorias"
                case 5:
                    return "sair"
                case _:
                    limpar_console()
                    mensagem_menu_inicial()
                    print("Opção inválida, digite um número entre 1 e 5!")
                    print()
                
def menu_inserir_evento(hash_table_categorias):
    """
    Cria e insere um novo evento para uma categoria especificada em uma dada hash table com categorias de eventos.
     
    Apenas insere se o evento criado ainda não existir para a categoria especificada.
    """
    
    from classes.Evento import Evento
    from classes.Categoria import Categoria

    nome_evento = input("Digite o nome do evento: ").lower()
    nome_categoria = input(f"Digite a categoria do evento '{nome_evento}': ").lower()

    eventos_categoria = hash_table_categorias.get_eventos_categoria(nome_categoria)

    if eventos_categoria:
        if eventos_categoria.existe_evento(nome_evento):
            print()
            print(f"O evento '{nome_evento}' já existe para a categoria '{nome_categoria}'.")
            print()
        else:
            descricao_evento = input(f"Digite a descrição do evento '{nome_evento}': ")
            evento = Evento(nome_evento, nome_categoria, descricao_evento)

            hash_table_categorias.get_eventos_categoria(nome_categoria).inserir_evento(evento)
            print()
            print(f"Evento '{nome_evento}' inserido com sucesso.")
            print()
    else:
        categoria = Categoria(nome_categoria)
        hash_table_categorias.inserir_categoria(categoria)

        descricao_evento = input(f"Digite a descrição do evento '{nome_evento}': ")
        evento = Evento(nome_evento, nome_categoria, descricao_evento)

        hash_table_categorias.get_eventos_categoria(categoria.getNome()).inserir_evento(evento)
        print()
        print(f"Evento '{nome_evento}' inserido com sucesso.")
        print()

def menu_remover_evento(hash_table_categorias):
    """
    Remove um evento de uma categoria especificada em uma dada hash table com categorias de eventos.
     
    Apenas remove se o evento existir para a categoria especificada, caso não, retorna:
    
    "O evento '{nome_evento}' não existe na tabela hash.".
    """
    
    nome_categoria = input(f"Digite a categoria do evento que deseja remover: ").lower() 

    if hash_table_categorias.get_eventos_categoria(nome_categoria):
        nome_evento = input("Digite o nome do evento que deseja remover: ").lower()
        
        if hash_table_categorias.get_eventos_categoria(nome_categoria).remover_evento(nome_evento) == nome_evento:
            print()
            print(f"Evento '{nome_evento}' removido com sucesso.")
            print()
    
    else:
        print()
        print(f"A categoria '{nome_categoria}' não está armazenada.")
        print()

if __name__ == "__main__":
    pass