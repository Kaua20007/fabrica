letra = 's'
while letra == 's':
    Altura = float(input('Digite sua altura (em metros, ex: 1.75): '))
    Peso = float(input('Digite seu peso (em kg, ex: 70.5): '))

        # Validações básicas para evitar divisões por zero ou valores negativos irreais
    if Altura <= 0 or Peso <= 0:
        print("Altura e peso devem ser valores positivos e maiores que zero. Tente novamente.")
        continue # Volta para o início do loop para pedir os dados novamente

    IMC = (Peso / Altura ** 2)
    IMC = round(IMC, 2)
    print ('O IMC é:', IMC)

    if IMC <= 18.4:
        print('Abaixo do peso')
    elif IMC <= 24.9:
        print('Peso Adequado')
    elif IMC <= 29.9:
        print('Sobrepeso')
    elif IMC <= 34.9:
        print('Obesidade Grau 1')
    elif IMC <= 39.9:
        print('Obesidade Grau 2')
    elif IMC >= 40: # Alterei para >= para pegar valores a partir de 40
        print('Obesidade Grau 3')

    letra = input('Deseja repetir o cálculo [s/n]? ').lower() # .lower() para aceitar 'S' ou 's'
    if letra not in ['s', 'n']:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        # Se você quiser que o loop termine para qualquer coisa diferente de 's',
        # você pode colocar 'letra = 'n'' aqui, ou apenas deixar como está,
        # e o loop só continua se for 's'.

print("Cálculo de IMC encerrado.")