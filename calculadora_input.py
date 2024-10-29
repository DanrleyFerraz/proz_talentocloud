def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = input("Digite o número da operação: ")

        if operacao == '0':
            print("Encerrando o programa.")
            break  
        elif operacao in ['1', '2', '3', '4']:
            try:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))

                if operacao == '1':
                    resultado = numero1 + numero2
                    print(f"Resultado: {numero1} + {numero2} = {resultado}")
                elif operacao == '2':
                    resultado = numero1 - numero2
                    print(f"Resultado: {numero1} - {numero2} = {resultado}")
                elif operacao == '3':
                    resultado = numero1 * numero2
                    print(f"Resultado: {numero1} * {numero2} = {resultado}")
                elif operacao == '4':
                    if numero2 != 0:
                        resultado = numero1 / numero2
                        print(f"Resultado: {numero1} / {numero2} = {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Digite apenas números válidos.")
        else:
            print("Essa opção não existe. Tente novamente.")
