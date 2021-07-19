
'''Escrever um prog que recebe dois num e um operador
matemático e com isso executa um calculo corretamente'''
def soma(num1 , num2): # criando função
    print('Somando', num1 + num2)
    resultado = num1 + num2
    return resultado

def subtracao(num1 , num2): # criando função
    print('Subtraindo', num1 - num2)
    resultado = num1 - num2
    return resultado

def multiplicacao(num1 , num2): # criando função
    print('mutiplicando', num1 * num2)
    resultado = num1 * num2
    return resultado

def divisao(num1 , num2): # criando função
    print('dividindo', num1 / num2)
    resultado = num1 / num2
    return resultado

if __name__ == '__main__':
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número:  '))
    operador = input('Informe um operador matemático: ')

    if operador == '+':
        resultado = soma(num1 , num2)
    elif operador == '-':
        resultado = subtracao(num1,num2)
    elif operador == '*':
        resultado = multiplicacao(num1,num2)
    elif operador == '/':
        resultado = divisao(num1, num2)
    else:
        print('Operador incorreto')

    print( f'O resultado da operação é: {resultado}')





''' minha forma de fazer
if __name__ == '__main__':
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número:  '))
    operador = input('Informe um operador matemático: ')

    if operador =='+':
        print('a soma dos números digitados é: ',num1 + num2)
    elif operador == '-':
        print('a subtração dos números digitados é: ', num1 - num2)
    elif operador == '/':
            print ('a adivisão dos números digitados é: ', num1 / num2)
    elif operador == '*':
        print('A multiplicação dos números é: ', num1 * num2)
    else:
        print('operador inválido' )'''