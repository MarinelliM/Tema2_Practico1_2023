class Reparacion:
    __patente: str
    __repacion: str
    __precioRepuesto: int
    __precioManoDeObra: int
    __estado: str

    def __init__(self,patente,repacion,precioRepuesto,precioManoDeObra,estado) -> None:
        self.__patente = patente
        self.__repacion = repacion
        self.__precioRepuesto = precioRepuesto
        self.__precioManoDeObra = precioManoDeObra
        self.__estado = estado
        pass

    def getpatente(self):
        return self.__patente
    
    def getreparacion(self):
        return self.__repacion
    
    def getpreciorep(self):
        return self.__precioRepuesto
    
    def getmano(self):
        return self.__precioManoDeObra
    
    def getsubtotal(self):
        return (self.__precioRepuesto+self.__precioManoDeObra)
    
    def getestado(self):
        return self.__estado
    
    def __eq__(self, otro):
        return self.getpatente() == otro
    
    def mostrar(self):
        return print('Patente: {}, Reparacion: {}, Precio de repuesto: {}, Precio de mano de obra: {}, Estado: {}' .format(self.getpatente(),self.getreparacion(),self.__precioRepuesto,self.__precioManoDeObra,self.__estado))