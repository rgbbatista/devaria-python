'''def Validar(valido1, valido2):
    #if valido1 == True and valido2 == True: # ou
    #if valido1 and valido2 == True: #ou
    if valido1  and valido2:
        return 'As duas variáveis são verdadeiras'
    else:
        return 'Não satisfez a condição'

if __name__ == '__main__':
     teste1= True
     teste2 = True


     respostaDafuncao = Validar(teste1, teste2)

     print(respostaDafuncao)'''


def Validar(valido1, valido2=True):#com parâmetro na variável

    if valido1 and valido2:
         return 'As duas variáveis são verdadeiras'
    else:
         return 'Não satisfez a condição'


if __name__ == '__main__':
     teste1 = True
     teste2 = False

     respostaDafuncao = Validar(teste1,)

     print(respostaDafuncao)

