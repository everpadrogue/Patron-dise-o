
from abc import ABC, abstractmethod

class Viaje(ABC):
    @abstractmethod
    def attak(self):
        pass

class Mexicano:
    def pasaporte(self):
        print("metodo pasaporte")
    def visa(self):
        print("metodo visa")


        
class VisaAdapter(Viaje):
    def __init__(self):
        self._mexicano = Mexicano()
        
    def visa(self):
        print("metodo visa")

class viajarUSA:
    def __init__(self):
        self.persona_mexicana = VisaAdapter()
        
