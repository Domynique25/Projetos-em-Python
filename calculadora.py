def calculadora():
  while True:
    print("calculadora simples")
    print()
    print("1 - Soma")
    print("2 - Substracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("s. sair")
    operacao = input("Selecione uma opcao ou 's' para sair:")
    if operacao == 's' or operacao == 'S':
      print("Obrigada por usar meu projeto <3 ")
      break
    
    if operacao not in ['1', '2', '3', '4']:
      print("Opcao invalida! Escolha uma opcao presente no menu")
      continue
    numero_1 = float(input("Primeiro numero: "))
    numero_2 = float(input("Segundo numero: "))
    
    if operacao == '1':
      resultado = numero_1 + numero_2
      print(" O resultado da operacao Soma e: ", resultado) 
    elif operacao == '2':
      resultado = numero_1 - numero_2
      print(" O resultado da operacao Substracao e: ", resultado) 
    elif operacao == '3':
      resultado = numero_1 * numero_2
      print(" O resultado da operacao Multiplicacao e: ", resultado) 
    else:
      if numero_2 == 0:
        print("Divisoes por zero nao sao possiveis. Tente novamente")
        continue
      else: 
        resultado = numero_1 / numero_2
        print(" O resultado da operacao Divisao e: ", resultado) 
calculadora()
