from estruturas_de_dados.HashTableCategoria import HashTableCategoria

from funcoes.menus import limpar_console
from funcoes.menus import menu_inicial
from funcoes.menus import menu_retorno
from funcoes.menus import mensagem_programa_encerrado
from funcoes.menus import menu_inserir_evento
from funcoes.menus import menu_remover_evento
from funcoes.menus import menu_buscar_evento

#from funcoes.testes import *

def main():

    categorias = HashTableCategoria()

    while True:
        escolha = menu_inicial()

        match(escolha):

            case "inserir_evento":
                limpar_console()
                menu_inserir_evento(categorias)
                
                if not menu_retorno():
                    mensagem_programa_encerrado()
                    break

            case "remover_evento":
                limpar_console()
                menu_remover_evento(categorias)
                
                if not menu_retorno():
                    mensagem_programa_encerrado()
                    break

            case "buscar_evento":
                limpar_console()
                menu_buscar_evento(categorias)
                
                if not menu_retorno():
                    mensagem_programa_encerrado()
                    break

            case "listar_categorias":
                limpar_console()
                print(categorias.listar_categorias())
                
                if not menu_retorno():
                    mensagem_programa_encerrado()
                    break

            case "sair":
                print()
                mensagem_programa_encerrado()
                break

if __name__ == "__main__":
    main()