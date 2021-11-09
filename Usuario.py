class Usuario:
    __idUsuario = 0
    __nomUsuario = ""
    __pasUsuario = ""
    __idEstado = 0

    def __init__(self):
        pass

    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getNomUsuario(self):
        return self.__nomUsuario
    
    def setNomUsuario(self, nomUsuario):
        self.__nomUsuario = nomUsuario

    def getPasUsuario(self):
        return self.__pasUsuario
    
    def setPasUsuario(self, pasUsuario):
        self.__pasUsuario = pasUsuario

    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idEstado):
        self.__idEstado = idEstado
