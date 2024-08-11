class Palabra:
    def __init__(self,id_palabra=None,palabra=None,definicion=None):
        self._id_palabra = id_palabra
        self._palabra = palabra
        self._definicion = definicion

    def __str__(self):
        return f'''
        ID = {self._id_palabra}
        PALABRA = {self._palabra}
        DEFINICION = {self._definicion}
        '''
    
    @property
    def id_palabra(self):
        return self.id_palabra
    
    @property
    def palabra(self):
        return self._palabra
    
    @property
    def definicion(self):
        return self._definicion
    
    @id_palabra.setter
    def id_palabra(self,id_palabra):
        self.id_palabra = id_palabra

    @palabra.setter
    def palabra(self,palabra):
        self._palabra = palabra

    @definicion.setter
    def definicion(self,definicion):
        self._definicion = definicion
