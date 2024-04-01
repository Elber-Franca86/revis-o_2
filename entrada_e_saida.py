def saudar():
    nome = input("Qual é o seu nome? ")
    print("Olá. ", nome,"! Seja bem-vindo(a)!")

saudar()


def somar():
    primeiro_numero = int(input("Digite o primeiro numero ")) #acrescenta p int para
    segundo_numero = int(input("Digite o segundo numero "))   #indicar que não é mais uma string
    soma = primeiro_numero + segundo_numero

    print("A soma dos numeros é: ", soma)

somar()

def multiplicar():
    num_1 = int(input ("Digite o primeiro numero "))
    num_2 = int(input("Digite o segundo numero "))
    multiplos = num_1 * num_2

    print("O produto dos numeros é: ", multiplos)

multiplicar()
