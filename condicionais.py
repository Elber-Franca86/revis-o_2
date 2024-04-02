def verifica_idade():
    idade = int(input("Qual a sua idade? "))
    if(idade >= 18):
        print("É maior de idade")
    else:
        print("É menor de idade")

verifica_idade()