from Cliente import Cliente
import csv

class ManejaC:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def initcliente(self):
        with open('clientes.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                apellido = str(fila[1])
                nombre = str(fila[2])
                telefono = int(fila[3])
                patente = str(fila[4])
                vehiculo = str(fila[5])
                estado = str(fila[6])
                cliente = Cliente(dni,apellido,nombre,telefono,patente,vehiculo,estado)
                self.agregarcliente(cliente)

    def agregarcliente(self,cliente):
        self.__lista.append(cliente)

    def test(self):
        for e in range(len(self.__lista)):
            self.__lista[e].mostrar()
        cliente1 = Cliente(123,'A','B',23,'AE2','fiat','T')
        cliente2 = Cliente(123,'A','B',23,'AE2','fiat','T')
        if cliente1 == cliente2:
            print(True)
        else: print(False)

    def Aa(self, dni, mr):
        i = 0
        while i < len(self.__lista):
            if dni == self.__lista[i].getdni():
                self.__lista[i].inciso1()
                patente = self.__lista[i].getpatente()
                mr.incisoa(patente)
                i = len(self.__lista)
            elif i<len(self.__lista) and dni != self.__lista[i].getdni():
                i+=1
        #if dni not in self.__lista:
        #    print('dni no encontrado')

    def cambiarestado(self,patente):
        i = 0
        while i < len(self.__lista):
            if patente == self.__lista[i].getpatente():
                self.__lista[i].setestado('T')
                self.__lista[i].mostrar()
                i = len(self.__lista)
            else: i+=1

    def mostrar(self,patente):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getpatente() == patente:
                return self.__lista[i].mostrar()
            else: i += 1

    def Ac(self,mr):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getestado() == 'P':
                patente = self.__lista[i].getpatente()
                self.mostrar(patente)
                mr.reparaciones(patente)
                i +=1
            else: i+=1

    def Ad(self):
        i = 0
        while i< len(self.__lista):
            cliente = self.__lista[i]
            for e in range(len(self.__lista)):
                if (cliente == self.__lista[e]) is True:
                    if cliente.getpatente() != self.__lista[e].getpatente():
                        cliente.mostrar()
            i += 1


