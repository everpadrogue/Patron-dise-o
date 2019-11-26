

from abc import ABC, abstractmethod


class Trabajador(ABC):
    def rutina_diaria(self):
         print("metodo rutina_diaria")
    
    def levanarse(self):
        print("metodo rutina_diaria")
    def comer(self):
        print("metodo rutina_diaria")

    def desayunar(self):
        print("metodo rutina_diaria")

    def trabajar(self):
        print("metodo rutina_diaria")
    def relajarse(self):
        print("metodo rutina_diaria")

    def ver_tv(self):
        print("metodo rutina_diaria")

    def dormir(self):
        print("metodo rutina_diaria")


class Contador(Trabajador):
    def trabajar(self):
        pass

    def comer(self):
        pass
    def ver_tv(self):
        pass

class Ingeniero(Trabajador):
    def desayunar(self):
        pass

    def trabajar(self):
        pass

    def comer(self):
        
        pass
    def dormir(self):
        pass

class Electricista(Trabajador):
    
    def levantarse(self):
        pass

    def trabajar(self):
        pass
    
    def relajarse(self):
        pass

    def comer(self):
        
        pass
    def dormir(self):
        pass

class profesor(Trabajador):
    def levantarse(self):
        pass
    def desayunar(self):
        pass

    def trabajar(self):
        pass

    def comer(self):
        pass
    def ver_tv(self):
        pass
    def dormir(self):
        pass

