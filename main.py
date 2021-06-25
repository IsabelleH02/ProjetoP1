import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")



while True:
    opcao = input("Opção - 1-Inserir / 2-Listar / 3-Inserir Avaliação/ 4-Mostrar avaliação/ 5-Sair: ")
    if (opcao == "1"):
        nome= input("Digite o nome da serie: ")
    if(opcao == "2"):
        for d in nome:
            print(d)
    if(opcao == "3"):
        avaliacao = input("digite avaliação: ")
    if(opcao == "4"):
        for d in avaliacao:
            print(d)
    if(opcao == "5") :
        break