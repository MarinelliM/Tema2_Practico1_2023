from Menu import menu
from ManejadorClientes import ManejaC
from ManejadorReparaciones import ManejaR
if __name__ == '__main__':

    ManejadorReparaciones = ManejaR()
    ManejadorReparaciones.initreparacion()
    ManejadorReparaciones.test()

    print('\n')

    ManejadorClientes = ManejaC()
    ManejadorClientes.initcliente()    
    ManejadorClientes.test()

    menu(ManejadorClientes,ManejadorReparaciones)

