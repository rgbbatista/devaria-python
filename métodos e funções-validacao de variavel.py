def Validar(valido):
    if valido == True:
        return 'O valor da variável é True'
    else:
        return 'o valor da variável é False'

if __name__ == '__main__':
     teste = False

     respostaDafuncao = Validar(teste)

     print(respostaDafuncao)
