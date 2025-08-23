letra = '1'
while letra == '1' :
    nome_produto = input('digite o nome do produto: ')
    valor_produto = float(input('digite o valor do produto: R$ '))
    qtd_produto = int(input(' Digite a quantidade do produto: '))

    with open('produto.txt','a') as arquivo:
        arquivo.write(f'{nome_produto} | {valor_produto} | {qtd_produto}')
    letra = input('deseja adisonar outro produto [1/2] '). lower()     
    if letra not in ['1','2']:
        print('pfv colocar "1" para continuar ou "2" para encerrar, SEU BURRO! ')

