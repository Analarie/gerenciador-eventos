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
                    return menu_inserir_evento()
                case 2:
                    return menu_remover_evento()
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

    nome_evento = input("Digite o nome do evento: ").lower()
    nome_categoria = input(f"Digite a categoria do evento '{nome_evento}': ").lower()

    eventos_categoria = hash_table_categorias.get_valor_categoria(nome_categoria)

    if eventos_categoria:
        pass
    
    #1 - conferir se a categoria existe
        #1.1 - se sim: conferir se o evento ja existe
            #1.1.1 se sim: "evento para categoria ja existe"
            #1.1.2 se nao: criar evento e adicionar à categoria
        #1.2 - se nao: criar categoria
            #1.2.1 adiciono categoria
        #1.3 - criar evento
        #1.4 - 
    
    nome_evento = input("Digite o nome do evento: ").lower()
    nome_categoria = input(f"Digite a categoria do evento '{nome_evento}': ").lower()
    descricao_evento = input(f"Digite a descrição do evento '{nome_evento}': ")

def menu_remover_evento():
    pass

if __name__ == "__main__":
    pass