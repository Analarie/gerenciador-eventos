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
    print("1 - VOLTAR")
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
            print("Opção inválida, digite um número entre 1 e 5!")
            print()

        else:
            match (escolha):
                case 1:
                    limpar_console()
                    return True
                case 2:
                    return False
                case _:
                    print("Opção inválida, digite um número entre 1 e 5!")
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
                    return "buscar_categoria"
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
    from classes.Evento import Evento
    from classes.Categoria import Categoria

    nome_evento = input("Digite o nome do evento: ").lower()
    nome_categoria = input(f"Digite a categoria do evento '{nome_evento}': ").lower()
    descricao_evento = input(f"Digite a descrição do evento '{nome_evento}': ")

    categoria = Categoria(nome_categoria)
    evento = Evento(nome_evento, categoria, descricao_evento)

    if hash_table_categorias.existe_categoria(categoria):
        #tratar essa inserção
        hash_table_categorias.getCategoria(categoria).inserir_evento(evento)
    else:
        #tratar essa inserção
        hash_table_categorias.inserir_categoria(categoria)

def menu_remover_evento():
    pass

if __name__ == "__main__":
    pass