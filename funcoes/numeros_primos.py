def gerar_numeros_primos(qtd_numeros):
    '''
    Retorna uma lista ordenada com uma quantidade N (qtd_numeros) de números primos.
    '''

    def eh_primo(numero):
        if numero % 2==0 and numero != 2:
            return False
        elif numero % 3==0 and numero != 3:
            return False
        elif numero % 5==0 and numero != 5:
            return False
        elif numero % 7==0 and numero != 7:
            return False
        else:
            return True

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

if __name__ == "__main__":
    pass