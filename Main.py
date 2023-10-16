from estruturas_de_dados.HashTableCategoria import HashTableCategoria

from funcoes.menus import menu_inicial

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
                print()
                print("VOU LISTAR!")
                break

            case "sair":
                print()
                print("PROGRAMA ENCERRADO!")
                break

    categorias = HashTableCategoria()

def test():
    from classes.Categoria import Categoria
    categorias = HashTableCategoria()

    hash1 = categorias.hash(Categoria("Computação"))
    hash2 = categorias.hash(Categoria("computação"))

    print(hash1, hash2, "\n")

    hash3 = categorias.hash(Categoria("informatica"))
    hash4 = categorias.hash(Categoria("fisioterapia"))

    print(hash3, hash4, "\n")

    hash5 = categorias.hash(Categoria("bioquimica"))
    hash6 = categorias.hash(Categoria("odontologia"))

    print(hash5, hash6, "\n")

    hash7 = categorias.hash(Categoria("sociologia"))
    hash8 = categorias.hash(Categoria("aociologis"))
    if hash7 == hash8:
         
        print(categorias.hash(Categoria("sociologia"))%9) 
    print(hash7, hash8, "\n")

    hash9 = categorias.hash(Categoria("administracao"))
    hash10 = categorias.hash(Categoria("sociologia"))

    print(hash9, hash10, "\n")

if __name__ == "__main__":
    test()
