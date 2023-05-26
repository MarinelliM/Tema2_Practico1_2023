def menu(MC,MR):
    print('1 -  Informar los datos del cliente y todas las reparaciones hechas al vehículo')
    print('2 -  Determinar si todas las reparaciones están terminadas')
    print('3 - Listar los datos de los clientes a los que no les han terminado el las reparaciones')
    print('4 - Determinar el o los clientes que le hacen servicio a más de un vehículo')
    print('0 - Salir')
    op = int(input('Ingrese la opcion a buscar:'))
    while op != 0:
        if op == 1:
            dni = int(input('Ingrese dni a buscar:'))
            MC.Aa(dni,MR)
        elif op == 2:
            patente = str(input('Ingrese patente a buscar:'))
            MR.Ab(patente,MC)
        elif op == 3:
            MC.Ac(MR)
        elif op == 4:
            MC.Ad()
        else:
            print('Opcion incorrecta')
            op = int(input('Ingrese la opcion a buscar:'))
        print('1 -  Informar los datos del cliente y todas las reparaciones hechas al vehículo')
        print('2 -  Determinar si todas las reparaciones están terminadas')
        print('3 - Listar los datos de los clientes a los que no les han terminado el las reparaciones')
        print('4 - Determinar el o los clientes que le hacen servicio a más de un vehículo')
        print('0 - Salir')
        op = int(input('Ingrese la opcion a buscar:'))
    print('Fin del programa')

