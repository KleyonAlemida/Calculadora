while True:
    print()
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Digite um operador para esse cálculo: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número. :D')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1+num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '/':
        print(num_1/num_2)
    elif operador == '*':
        print(num_1*num_2)
    else:
        print('Operador inválido.')

    continuar = input('Deseja seguir com mais alguma conta? [S] Sim ou [N] Não: ')
    if continuar.upper() == 'N':
        print('Você optou por sair do programa ;-;')
        break
