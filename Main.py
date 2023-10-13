from estruturas_de_dados.HashTableCategoria import HashTableCategoria
from funcoes.menus import menu_inicial

def main():

    categorias = HashTableCategoria()

    while True:
        escolha = menu_inicial()

        match(escolha):
            case "inserir_evento":
                print()
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
                print()
                print("VOU LISTAR!")
                break

            case "sair":
                print()
                print("PROGRAMA ENCERRADO!")
                break

    categorias = HashTableCategoria()

if __name__ == "__main__":
    main()