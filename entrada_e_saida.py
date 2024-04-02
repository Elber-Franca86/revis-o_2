def saudar():
    print("===SAUDAÇÃO===")
    nome = input("Qual é o seu nome? ")
    print("Olá. ", nome,"! Seja bem-vindo(a)!")

saudar()


def somar():
    print("====Soma===")
    primeiro_numero = float(input("Digite o primeiro numero: ")) #acrescenta p int para
    segundo_numero = float(input("Digite o segundo numero: "))   #indicar que não é mais uma string
    soma = primeiro_numero + segundo_numero

    print("A soma dos numeros é: ", soma)

somar()

def multiplicar():
    print("===Multiplicação===")
    num_1 = int(input ("Digite o primeiro numero: "))
    num_2 = int(input("Digite o segundo numero: "))
    multiplos = num_1 * num_2

    print("O produto dos numeros é: ", multiplos)

multiplicar()


def divisao():
    print("===Divisão===")
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite o segundo numero: "))
    dividendo = n1 / n2
    print("A divisão do numero", str(n1),  "por dois é: ", dividendo)

divisao()


def indice_de_massa():
    print("===IMC===")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso/(altura*altura)
    print("O seu Imc é: ", str(imc))    

indice_de_massa()