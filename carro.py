from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, numero_de_portas):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.numero_de_portas = numero_de_portas
        self.lista_carro = [f' FABRICANTE DO CARRO - {fabricanteveiculo}',f' NUMERO DE RODAS - {numerorodas}',
                            f' TIPO DO VEICULO - {tipoveiculo}',f' NUMERO DE PORTAS - {numero_de_portas}']

    def getValores(self,dic):
        dic['PLACA DO CARRO - '+ self._placaVeiculo] = self.lista_carro[:]

    def imprime(self,dic):
        print(dic)
    def remove(self,placaveiculo, dic):
        if dic.get('PLACA DO CARRO - '+placaveiculo) is not None:
            del dic['PLACA DO CARRO - '+placaveiculo]



    def pesquisar(self, placaveiculo,dic):
        if dic.get('PLACA DO CARRO - '+placaveiculo) is not None:
            print(dic.get('PLACA DO CARRO - '+placaveiculo))

