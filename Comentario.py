class Comentario:
    __idComentario = 0
    __idUsuario = 0
    __nomUsuario = ""
    __desComentario = ""
    __idNoticia = 0
    __nomNoticia = ""
    __idEstado = 0

    def __init__(self):
        pass

    def getIdComentario(self):
        return self.__idComentario
    
    def setIdComentario(self, idComentario):
        self.__idComentario = idComentario
    
    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getNomUsuario(self):
        return self.__nomUsuario
    
    def setNomUsuario(self, nomUsuario):
        self.__nomUsuario = nomUsuario

    def getDesComentario(self):
        return self.__desComentario
    
    def setDesComentario(self, desComentario):
        self.__desComentario = desComentario

    def getIdNoticia(self):
        return self.__idNoticia
    
    def setIdNoticia(self, idNoticia):
        self.__idNoticia = idNoticia

    def getNomNoticia(self):
        return self.__nomNoticia
    
    def setNomNoticia(self, nomNoticia):
        self.__nomNoticia = nomNoticia

    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idEstado):
        self.__idEstado = idEstado
