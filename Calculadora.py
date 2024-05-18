while True:
    # Menu de opções se repete até que a condição sai seja verdadeira
    print('[1] - Somar')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Sair\n')

    try:
        # Pede ao usuário que informe a opção desejada
        opcao = int(input('Escolha a opção desejada: '))

        # Executa a primeira condição informada pela opção 1
        if opcao == 1:
            print('Você escolheu a opção Somar\n')
            num1 = int(input('Informe o primeiro numero: '))
            num2 = int(input('Informe o segundo numero: '))
            somar = num1 + num2
            print(f'[RESULTADO] = {somar}\n')

        # Executa a primeira condição informada pela opção 2
        elif opcao == 2:
            print('Você escolheu a opção Subtrair\n')
            num1 = int(input('Informe o primeiro numero: '))
            num2 = int(input('Informe o segundo numero: '))
            subtrair = num1 - num2
            print(f'[RESULTADO] = {subtrair}\n')

        # Executa a primeira condição informada pela opção 3
        elif opcao == 3:
            print('Você escolheu a opção Multiplicar\n')
            num1 = int(input('Informe o primeiro numero: '))
            num2 = int(input('Informe o segundo numero: '))
            multiplicar = num1 * num2
            print(f'[RESULTADO] = {multiplicar}\n')

        # Executa a primeira condição informada pela opção 4
        elif opcao == 4:
            print('Você escolheu Sair')
            break
    
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.\n')
