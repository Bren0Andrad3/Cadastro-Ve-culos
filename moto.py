from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,cilindrada):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.cilindrada = cilindrada
        self.lista_moto = [f' FABRICANTE DA MOTO - {fabricanteveiculo}', f' NUMERO DE RODAS - {numerorodas}',
                            f' TIPO DO VEICULO - {tipoveiculo}', f' NUMERO DE CILINDRADA - {cilindrada}']

    def getValores(self,dic):
        dic['PLACA DA MOTO - '+ self._placaVeiculo] = self.lista_moto[:]

    def imprime(self,dic):
        print(dic)

    def remove(self, placaveiculo, dic):
        if dic.get('PLACA DA MOTO - '+placaveiculo) is not None:
            del dic['PLACA DA MOTO - '+placaveiculo]


    def pesquisar(self, placaveiculo,dic):
        if dic.get('PLACA DA MOTO - '+placaveiculo) is not None:
            print(dic.get('PLACA DA MOTO - '+placaveiculo))
