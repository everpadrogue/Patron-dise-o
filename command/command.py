

from abc import ABC, abstractmethod

class Celular(ABC):
    @abstractmethod
    def action(self):
        pass

class Ver_Redes_sociales(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.Ver_Redes_sociales()


class escuchar_music(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.escuchar_music()


class ver_videos(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.ver_videos()

      
class enviar_archivos(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.enviar_archivos()

class ActionMenu:
    def Ver_Redes_sociales(self):
        pass
        
    def escuchar_music(self):
        pass
        
    def ver_videos(self):
        pass

    def enviar_archivos(self):
        pass

class Action:
    def __init__(self):
        self._actions = []

    def executar_tareas(self, Celular):
        self._actions.append(Celular)
        Celular.action()


class main():
    menu = ActionMenu()
    celular_Ver_Redes_sociales = Ver_Redes_sociales(menu)
    celular_escuchar_music = escuchar_music(menu)
    celular_ver_videos = ver_videos(menu)
    celular_enviar_archivos = enviar_archivos(menu)

    act = Action()
    act.executar_tareas(celular_Ver_Redes_sociales)
    act.executar_tareas(celular_escuchar_music)
    act.executar_tareas(celular_ver_videos)
    act.executar_tareas(celular_enviar_archivos)
