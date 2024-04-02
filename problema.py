def menu():
    print("Operações:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    else:
        print("Essa opção não existe.")

while True:
    menu()
    opcao = int(input("Digite o numero da operação desejada (0 para sair): "))

    if opcao == 0:
        print("Encerrando o programa.")
        break
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    resultado = calculadora(num1, num2,opcao)
    if resultado is not None:
        print(f"Resultado: {resultado}\n")

