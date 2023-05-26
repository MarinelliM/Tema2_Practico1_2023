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
            #opcion1(MC,dni,MR)
        elif op == 2:
            patente = str(input('Ingrese patente a buscar:'))
            MR.Ab(patente,MC)
            #opcion2(patente,MR,MC)
        elif op == 3:
            MC.Ac(MR)
            #opcion3(MC,MR)
        elif op == 4:
            MC.Ad()
            #opcion4(MC)
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

def opcion1(mc,dni,mr):
        i = 0
        lista = str
        total = 0
        a = 0
        while i < len(mc):
            if mc[i].getdni() == dni:
                lista = mc[i].getpatente()
                i+=1
            else: i+=1
        while a < len(mc):
            if lista == mr[a].getpatente():
                total += mr[a].getsubtotal() 
                print('Dni:{}\t\t\tApellido y Nombre:{}'.format(mc[a].getdni(),mc[a].getnombrecompleto()))
                print('Patente:{}\t\t\tVehiculo:{}'.format(mc[a].getpatente(),mc[a].getvehiculo()))
                print('Reparacion:\t\t\tprecio repuesto:\t\t\tmano de obra:\t\t\tsubtotal:')
                print('{}\t\t\t${}\t\t\t${}\t\t\t${}'.format(mr[a].getreparacion(),mr[a].getpreciorep(),mr[a].getmano(),mr[a].getsubtotal()))
                #print('\t\t\t\t\t\tTOTAL A PAGAR:{}'mr[a].gettotal())
                a = len(mc)
            else: a+=1

def opcion2(patente,mr,mc):
    i = 0
    a = True
    e = 0
    while i < len(mr):
        if mr[i].getpatente() == patente and mr[i].getestado() == 'T':
            a = True
        elif mr[i].getpatente()== patente and mr[i].getestado() != 'T':
            a = False    
        else: i+=1
    while e < len(mc):
        if a == True and mc[e].getpatente() == patente:
            mc[e].setestado('T')
            mc[e].mostrar()




def opcion3(mc,mr):
    i = 0
    while i < len(mc):
        if mc[i].getestado() != 'T':
            print('Apellido y Nombre: {}\t\t\tTelefono:{}'.format(mc[i].getnombrecompleto(),mc[i].gettelefono()))
            print('Patente:{}\t\t\tVehiculo:{}'.format(mc[i].getpatente(),mc[i].getvehiculo()))

def opcion4(mc):
    i = 0
    while i < len(mc):
        if mc[i] == mc[i+1]:
            mc[i].mostrar()
