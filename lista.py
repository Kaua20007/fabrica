nomes = ['joaquin','maria',' ana']
print('lista inicial', nomes)
print('-' * 50)
#adicionando elementos
nomes.append('carlos') #adicional ao final
print('após append', nomes)
print('-' * 50)
nomes.insert(1,'fernanda')#insere fernanda na posisão um
print('após insert, nomes')
print('-' * 50)

#motificando elementos
nomes[2] = 'paulo' #motifica o elemto do indice 2
print('após motificação:',nomes)

#removendo elementos
del nomes [3] #remove o elemento do indice 3
print('aposdel:',nomes)
nomes.remove('paulo')
print('apos o remove:', nomes)
print('-' * 50)

removido = nomes.pop(2)#remove e retorna o elemento no indice 2
print(f'após pop ( removido"{removido}"):', nomes)
print('-' * 50)

nomes.clear() # ESVAZIA A LISTA
print('após clear:',nomes)
print('-' * 50)
