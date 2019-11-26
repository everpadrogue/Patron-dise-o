
import abc


class Tienda:

    def __init__(self):
        self._ventas = []

    def Abarrotes(self, solicitud):
        self._ventas.append(solicitud)

    def verduras(self):
        for solicitud in self._ventas:
            solicitud.compra_producto()


class Solicitud(metaclass=abc.ABCMeta):
    def __init__(self, recibir):
        self._recibir = recibir

    @abc.abstractmethod
    def compra_producto(self):
        pass


class Compras(Solicitud):
  

    def compra_producto(self):
        self._recibir.pago()


class Recibir:
    def pago(self):
        pass


def main():
    recibir = Recibir()
    compras = Compras(recibir)
    tienda = Tienda()
    tienda.Abarrotes(compras)
    tienda.verduras()


if __name__ == "__main__":
    main()
