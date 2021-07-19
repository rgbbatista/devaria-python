if __name__ == '__main__':

    valido = False
    print(valido)
    print(not valido)
    print(not True)


    print('exemplo de operador E ou and')
def SecondOperand():
    print('Avaliando segundo o operador')
    return True


if __name__ == '__main__':
    a = False and SecondOperand()
    print(a)
#o primeiro é falso nem analiza a segunda condição
    b = True and SecondOperand()
    print(b)
# o primeiro é verdadeiro analiza a segunda condicao


    print('exemplo de operador or ou')
def SecondOperand():
    print('Avaliando segundo o operador')
    return True


if __name__ == '__main__':
    a = False or SecondOperand()
    print(a)

    b = True or SecondOperand()
    print(b)


