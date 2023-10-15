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
    hash8 = categorias.hash(Categoria("matemática"))

    print(hash7, hash8, "\n")

    hash9 = categorias.hash(Categoria("administracao"))
    hash10 = categorias.hash(Categoria("medicina"))

    print(hash9, hash10, "\n")

def test2():
    from classes.Categoria import Categoria
    hashTableCategoria = HashTableCategoria()

    cat1 = Categoria("medicinaa")
    cat2 = Categoria("computacaoa")
    cat3 = Categoria("educacaaa")

    hashTableCategoria.inserir_categoria(cat1)
    hashTableCategoria.inserir_categoria(cat2)
    hashTableCategoria.inserir_categoria(cat3)

    print(hashTableCategoria.chaves)
    print(hashTableCategoria.valores)

def test3():

    from classes.Categoria import Categoria

    hashTableCategoria = HashTableCategoria()

    categoria = Categoria("cat")
    print(hashTableCategoria.hash(categoria))

    categoria2 = Categoria("tac")
    print(hashTableCategoria.hash(categoria2))

def test4():
    """
    Testando a função HashTableCategoria.dobrar_tamanho()
    """

    from classes.Categoria import Categoria
    hash_table_categoria = HashTableCategoria()

    cat1 = Categoria("medicinaa")
    cat2 = Categoria("computacaoa")
    cat3 = Categoria("educacaaa")

    hash_table_categoria.inserir_categoria(cat1)
    hash_table_categoria.inserir_categoria(cat2)
    hash_table_categoria.inserir_categoria(cat3)

    print(hash_table_categoria.chaves, len(hash_table_categoria.chaves))
    print(hash_table_categoria.valores, len(hash_table_categoria.valores))

    hash_table_categoria.dobrar_tamanho()
    print()

    print(hash_table_categoria.chaves, len(hash_table_categoria.chaves))
    print(hash_table_categoria.valores, len(hash_table_categoria.valores))

if __name__ == "__main__":
    main()