def verifica_idade():
    idade = int(input("Qual a sua idade? "))
    if(idade >= 18):
        print("É maior de idade")
    else:
        print("É menor de idade")

verifica_idade()

def par_impar():

    numero = int(input("Digite um número: "))
    if (numero % 2 == 0):
        print("O número", str(numero), "é par.")
    else:
        print("O numero", str(numero), "é impar.")

par_impar()