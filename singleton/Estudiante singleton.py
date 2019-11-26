'''
un ejemplo simple de uso de Singleton
'''
class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance

	
class Estudiante(Singleton):
	nombre = u""
		
_estudiante = Estudiante()
_estudiante_1 = Estudiante()
 
_estudiante.nombre = u"Veronica"
_estudiante_1.nombre = u"Everardo"
print(_estudiante.nombre, _estudiante_1.nombre)
