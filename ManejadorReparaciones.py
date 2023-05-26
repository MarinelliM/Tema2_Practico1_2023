from Reparacion import Reparacion
import csv

class ManejaR:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def initreparacion(self):
        with open('reparaciones.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                patente = str(fila[0])
                reparacion = str(fila[1])
                precioRepuesto = int(fila[2])
                precioManoDeObra = int(fila[3])
                estado = str(fila[4])
                reparacione = Reparacion(patente,reparacion,precioRepuesto,precioManoDeObra,estado)
                self.agregarreparacion(reparacione)

    def agregarreparacion(self,reparacion):
        self.__lista.append(reparacion)

    def test(self):
        for e in range(len(self.__lista)):
            self.__lista[e].mostrar()

    def incisoa(self,patente):
        i = 0
        total = 0
        while i < len(self.__lista):
            if patente == self.__lista[i].getpatente():
                prepuesto = int(self.__lista[i].getpreciorep())
                pmano = int(self.__lista[i].getmano())
                subtotal = int(prepuesto) + int(pmano)
                total += int(subtotal)
                print('Reparacion:\t\t\tprecio repuesto:\t\t\tmano de obra:\t\t\tsubtotal:')
                print('{}\t\t\t${}\t\t\t${}\t\t\t${}'.format(self.__lista[i].getreparacion(),prepuesto,pmano,subtotal))
                i += 1
            else: i+=1
        if  patente not in self.__lista:
            return print('No se encontro la patente')
        else: 
            print('TOTAL A PAGAR: ${}' .format(total))

    def Ab(self,patente,mc):
        i = 0
        bandera = True
        while i < len(self.__lista):
            if patente == self.__lista[i].getpatente() and self.__lista[i].getestado() != 'T':
                bandera = False
                print('Tiene reparaciones pendientes')
                i = len(self.__lista)
            else: i += 1
        if bandera == True:
            mc.cambiarestado(patente)
            i = 0
            total = 0
            while i < len(self.__lista):
                if patente == self.__lista[i].getpatente():
                    prepuesto = int(self.__lista[i].getpreciorep())
                    pmano = int(self.__lista[i].getmano())
                    subtotal = int(prepuesto) + int(pmano)
                    total += int(subtotal)
                    i+=1
                else: i+=1
            print('TOTAL A PAGAR: ${}' .format(total))

    def reparaciones(self,patente):
        for e in range(len(self.__lista)):
            if patente == self.__lista[e].getpatente():
                print('Reparacion: {}'.format(self.__lista[e].getreparacion()))

