from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,marchas):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.marchas = marchas
        self.lista_bike = [f' FABRICANTE DO CARRO - {fabricanteveiculo}', f' NUMERO DE RODAS - {numerorodas}',
                            f' TIPO DO VEICULO - {tipoveiculo}', f' NUMERO DE MARCHAS - {marchas}']

    def getValores(self, dic):
        dic['PLACA DA BICICLETA - '+ self._placaVeiculo] = self.lista_bike[:]

    def imprime(self, dic):
        print(dic)

    def remove(self,placaveiculo, dic):
        if dic.get('PLACA DA BICICLETA - '+placaveiculo) is not None:
            del dic['PLACA DA BICICLETA - '+placaveiculo]

    def pesquisar(self, placaveiculo,dic):
        if dic.get('PLACA DA BICICLETA - '+placaveiculo) is not None:
            print('PLACA DA BICICLETA - '+dic.get(placaveiculo))
