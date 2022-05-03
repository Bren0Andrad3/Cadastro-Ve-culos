from Veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta

opcao = 0
contador_carro = 0
contador_moto = 0
contador_bike = 0
dic_carro = {}
dic_moto = {}
dic_bike = {}
while(opcao != 5):

    print('Bem vindo ao menu')
    print(" ----------------------------------- \n")
    print("1 --- INSERIR INFORMAÇÕES DO VEICULO \n")
    print("2 --- IMPRIMIR LISTA DE TODOS OS VEICULOS \n")
    print("3 --- PESQUISAR VEICULOS \n")
    print("4 --- REMOVER VEICULOS\n")
    print("5 --- SAIR\n")

    opcao = int(input('Digite a opção desejada\n'))

    if opcao == 1:
        placaveiculo = input("INSERIR A PLACA DO VEICULO \n")
        fabricanteveiculo = input("INSERIR A FABRICANTE DO VEICULO \n")
        numerorodas = input("INSERIR O NUMERO DE RODAS DO VEICULO \n")
        tipoveiculo = input("INSERIRO TIPO DO VEICULO(EX. carro ou moto ou bicicleta) \n")
        tipoveiculo = tipoveiculo.lower()

        if tipoveiculo == 'carro':

            contador_carro = 1
            numero_de_portas = input("INSERIR O NUMERO DE PORTAS DO CARRO \n")
            carro1 = Carro(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, numero_de_portas)
            carro1.getValores(dic_carro)

        if tipoveiculo == 'moto':
            contador_moto = 1
            cilindrada = input("INSERIR AS CILINDRADAS DA MOTO \n")
            moto1 = Moto(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, cilindrada)
            moto1.getValores(dic_moto)
        if tipoveiculo == 'bicicleta':
            contador_bike = 1
            marchas = input("INSERIR AS MARCHAS DA BICICLETA \n")
            bike1 = Bicicleta(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, marchas)
            bike1.getValores(dic_bike)

    if opcao == 2:
        if contador_carro == 1:
            carro1.imprime(dic_carro)
        if contador_moto == 1:
            moto1.imprime(dic_moto)
        if contador_bike == 1:
            bike1.imprime(dic_bike)

    if opcao == 3:
        pesquisa = input('INSIRA A PLACA DO VEICULO QUE DESEJA BUSCAR\n')
        if contador_carro == 1:
            carro1.pesquisar(pesquisa,dic_carro)
        if contador_moto == 1:
            moto1.pesquisar(pesquisa,dic_moto)
        if contador_bike == 1:
            bike1.pesquisar(pesquisa,dic_bike)

    if opcao == 4:
        remover = input('INSIRA A PLACA DO VEICULO QUE DESEJA REMOVER\n')
        if contador_carro == 1:
            carro1.remove(remover, dic_carro)
        if contador_moto == 1:
            moto1.remove(remover, dic_moto)
        if contador_bike == 1:
            bike1.remove(remover, dic_bike)




