import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ProjP1"]
mycol = mydb["customers"]


while True:
    opcao = input("Opção - 1-Inserir manualmente / 2-Ler arquivo CSV e inserir no bd/ "
                  "3-Ler Dados e criar arquivo *.txt / 4-Sair: ")
    if (opcao == "1"):
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o telefone do novo contato: ")

        mydict = {"nome": nome, "telefone": telefone}

        x = mycol.insert_one(mydict)
        break

    if(opcao =="2"):

        arquivo = open('D:\\python-SI\\dados.csv', 'r')
        lines = arquivo.readlines()
        for l in lines:
            coluna = l.split(';')
            print("Codigo: " + coluna[0])
            print("Nome: " + coluna[1])
            print("Telefone: " + coluna[2])
            print("*******************************")

        codigo = coluna[0]
        nome = coluna[1]
        telefone = coluna[2]

        mydict = {"nome": nome, "codigo": codigo, "telefone": telefone}

        x = mycol.insert_one(mydict)

        print(x.inserted_id)
        break

    if(opcao =="3"):

        lst = mycol.find({},{"_id": 0})
        for x in lst:
            print(x)

        arq = open('C:/tmp/agenda.txt', 'w')
        texto = []
        texto.append('Agenda\n')
        texto.append('--------------- \n')
        texto.append(x)
        arq.writelines(texto)
        arq.close()

        arq = open('C:/tmp/agenda.txt', 'r')
        texto = arq.read()
        print(texto)
        break

    if (opcao =="4"):

        break
