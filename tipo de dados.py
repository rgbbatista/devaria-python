print('Olá Mundo')

def print_hi(name):
    print(f'óla mundo, {name}')
if __name__ == '__main__':
    print_hi('Rodrigo')
#TIPOS DE DADOS: str,list,tuple,dict,int,float,complex,bool

temperatura= 20
print(temperatura)
print(type(temperatura))
temperatura= 'Rodrigo'
print(temperatura)
print(type(temperatura))

listaNomes = ['Rodrigo','Ricardo','Érica','Ellen']
print(listaNomes)
print(type(listaNomes))

dicionarioPessoa = {
    'nome': 'Rodrigo',
    'idade': '35',
     'peso': '63kg'
}
print(dicionarioPessoa)
print(type(dicionarioPessoa))

numeroComplexo = 5 + 5j
print(type(numeroComplexo))

verificacao = False # False True sempre com letra maiuscula
print(type(verificacao))

variavelNulo = None
print(type(variavelNulo))


numero = input('digite um número:')
print(f'  número digitado foi {numero}')
print(type(numero))
#input por padrao é uma str
#para mudar o tipo de str para int
numero = int(input('digite um número:'))
print(type(numero))
