class Noticia:
    __idNoticia = 0
    __titNoticia = ""
    __idEstado = 0

    def __init__(self):
        pass

    def getIdNoticia(self):
        return self.__idNoticia
    
    def setIdNoticia(self, idNoticia):
        self.__idNoticia = idNoticia

    def getTitNoticia(self):
        return self.__titNoticia
    
    def setTitNoticia(self, titNoticia):
        self.__titNoticia = titNoticia

    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idEstado):
        self.__idEstado = idEstado
