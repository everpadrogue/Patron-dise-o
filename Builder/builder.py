from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Construir(ABC):

    @abstractproperty
    def casa(self) -> None:
        pass
    @abstractmethod
    def tabicon(self) -> None:
        pass
    @abstractmethod
    def cemento(self) -> None:
        pass
    @abstractmethod
    def material_herramientas(self) -> None:
        pass

#######################################################
class Elementos_construccion(Construir):

    def __init__(self) -> None:

        self.constructor()

    def constructor(self) -> None:
        self._casa = Casah()

    @property
    def casa(self) -> Casah:

        casa = self._casa
        self.constructor()
        return casa

    def tabicon(self) -> None:
        self._casa.add("Tabicon")

    def cemento(self) -> None:
        self._casa.add("cemento")

    def material_herramientas(self) -> None:
        self._casa.add("material de herramientas")


class Casah():

    def __init__(self) -> None:
        self.herramientas = []

    def add(self, part: Any) -> None:
        self.herramientas.append(part)

    def material(self) -> None:
        print(f"Product herramientas: {', '.join(self.herramientas)}", end="")


class Empresa_construccion:


    def __init__(self) -> None:
        self._construir = None

    @property
    def construir(self) -> Construir:
        return self._construir

    @construir.setter
    def construir(self, construir: Construir) -> None:

        self._construir = construir


    def mapa_construccion(self) -> None:
        self.construir.tabicon()

    def cimiento(self) -> None:
        self.construir.tabicon()
        self.construir.cemento()
        self.construir.material_herramientas()

######################################################
if __name__ == "__main__":

    empresa_construccion = Empresa_construccion()
    construir = Elementos_construccion()
    empresa_construccion.construir = construir
