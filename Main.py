from estruturas_de_dados.HashTableCategoria import HashTableCategoria

from funcoes.menus import limpar_console, menu_inicial, menu_retorno, mensagem_programa_encerrado
from funcoes.testes import *

def main():

    categorias = HashTableCategoria()

    while True:
        escolha = menu_inicial()

        match(escolha):
            case "inserir_evento":
                
                print("VOU INSERIR!")
                break

            case "remover_evento":
                print()
                print("VOU REMOVER!")
                break

            case "buscar_categoria":
                print()
                print("VOU BUSCAR!")
                break

            case "listar_categorias":
                limpar_console()
                print(categorias.listar_categorias())
                
                if not menu_retorno():
                    mensagem_programa_encerrado()
                    break

            case "sair":
                mensagem_programa_encerrado()
                break

if __name__ == "__main__":
    main()