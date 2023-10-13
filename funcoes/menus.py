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
                
                    
