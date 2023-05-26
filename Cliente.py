class Cliente:
    __dni: int
    __apellido: str
    __nombre: str 
    __telefono: int 
    __patente: str 
    __vehiculo: str  
    __estado: str

    def __init__(self,dni,apellido,nombre,telefono,patente,vehiculo,estado) -> None:
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado
        pass

    def getpatente(self):
        return self.__patente
    
    def getvehiculo(self):
        return self.__vehiculo
    
    def getdni(self):
        return self.__dni
    
    def gettelefono(self):
        return self.__telefono
    
    def inciso1(self):
        return print('Dni: {}, Apellido y Nombre: {} \n Patente: {}, Vehiculo: {}' .format(self.getdni(),self.getnombrecompleto(),self.getpatente(),self.getvehiculo()))
    
    def getnombrecompleto(self):
        return self.__apellido+ ' ' +self.__nombre
    
    def getestado(self):
        return self.__estado
    
    #def __eq__(self,otro):
    #    return (self.getdni() == otro)
    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return (
                self.getdni() == otro.getdni() and
                self.getnombrecompleto() == otro.getnombrecompleto() and
                self.gettelefono() == otro.gettelefono()
            )
        return False
    
    def setestado(self, estado:str):
        self.__estado = estado
    
    def mostrar(self):
        return print('Dni: {}, Apellido: {}, Nombre: {}, Telefono: {}, Patente: {}, Vehiculo: {}, Estado: {}' .format(self.getdni(),self.__apellido,self.__nombre,self.__telefono,self.getpatente(),self.__vehiculo,self.__estado))
    
