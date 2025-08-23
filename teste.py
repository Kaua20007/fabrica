# ao tenta apresentar um odigo que contenha erro 
try: 
    #solicite ao usuario 2 números para a divisão
    NUM1 = float(input('digite um numero: '))
    num2 = float(input('digite outro numero: '))
    resultado = NUM1 / num2

# se o erro do usuario for digitar em texto
except ValueError:
        print('digite em algaritimo ')

#se o erro for por dividir o 0
except ZeroDivisionError:
    print('divisã por zero não existe')

#caso seja outro erro não detectado pelo sistema que criamos
except:
    print('digite um valor valido')   
#se estiver certo a conta terminar a operação
else:
     print(f'o resultado da divisão é {resultado}')
finally:
     print('operação finalizada')
