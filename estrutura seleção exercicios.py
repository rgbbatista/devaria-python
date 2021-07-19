
  #Escrever um prog que recebe o nome e a idade
#de acordo com uma lista de convidados, validar
#se a pessoa está na lista e se é maior de idade,
#e retornar a mensagem de acordo com as validações
#feitas

if __name__ == '__main__':


  listaConvidados =['Rodrigo','Ricardo','Ellen','Érica']
  print(listaConvidados)

  nome= input('Qual seu nome: ')
  idade=int(input('Qual a sua idade: '))

  estaNalista = nome in listaConvidados
  maiorIdade = idade >=18

  if estaNalista:
    if maiorIdade:
      print( nome, 'Bem vindo! Fostes convidado e é maior de idade')
    else:
     print(nome,'Desculpa, seu nome está na lista mas você não é maior de idade')
  else:
     print(nome,'Desculpa, mas seu nome não está na lista ou é menor de idade')

