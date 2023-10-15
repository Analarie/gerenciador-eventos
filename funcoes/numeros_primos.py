def eh_primo(numero):
    comeco = 2

    while comeco <= numero**(1/2):
        if numero % comeco < 1:
            return False
        comeco += 1

    return numero > 1

def gerar_numeros_primos(qtd_numeros):
    """
    Retorna uma lista ordenada com uma quantidade N (qtd_numeros) de números primos.
    """

    primos = []
    primo = 2

    if qtd_numeros > 0:
        primos.append(primo)
        primo += 1

    while len(primos) < qtd_numeros:
        if eh_primo(primo):
            primos.append(primo)
        
        primo += 2

    return primos

def primo_sucessor(numero):
    """
    Recebe um número e retorna o próximo primo maior ou igual a ele.
    """
    aux = numero

    while True:
        if eh_primo(aux):
            return aux
        
        aux += 1

def primo_antecessor(numero):
    """
    Recebe um número e retorna o próximo primo menor ou igual a ele.
    """
    aux = numero

    while True:
        if eh_primo(aux):
            return aux
        
        aux -= 1

if __name__ == "__main__":
    pass
