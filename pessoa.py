#Solicitando o email e o nome para o cadastro do usuario
nome_completo = input('escreva o nome: ')
email = input('escreva o seu  email: ')

#Criando o arquivo pessoa.txt para gravação dos dados
arquivo = open('pessoa;txt', 'a')
arquivo.write(f'{nome_completo} | {email}\n')
arquivo.close()