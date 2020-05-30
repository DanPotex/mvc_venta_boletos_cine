class View:
    """
    ******************************************************
    * Vista de la BD de una Sistema de Venta de Boletos  *
    ******************************************************
    """

    #Funcion de Inico
    def start(self):
        print('============================')
        print('= ¡Bienvenido al Cinemex!  =')
        print('============================')
    
    #Funcion de Fin de Programa
    def end(self):
        print('=================================')
        print('=       ¡Hasta la vista!        =')
        print('=================================')

    #Funcion del Menu
    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Clientes')
        print('2. Peliculas')
        print('3. Sala')
        print('4. Asientos')
        print('5. Mostrar')
        print('6. Compra')
        print('7. Tickets')
        print('8. Salir')

    #Funcion Opcion
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    #Funcion "No Valida"
    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')

    #Funcion de Pregunta algo de Usuario
    def ask(self, output):
        print(output, end = '')

    #Funcion de Mensaje de Pantalla
    def msg(self, output):
        print(output)

    #Funcion de OK (si algo se hizo correcto en el programa)
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    #Funcion de Error (si algo sale mal en alguna operacion en el programa)
    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    *********************
    * Views for Cliente *
    *********************
    """

    #Funcion para el Menu de los Clientes
    def cliente_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1. Agregar Cliente')
        print('2. Leer Cliente')
        print('3. Leer todos los Clientes')
        print('4. Leer todos los Clientes por Telefono')
        print('5. Actualizar Cliente')
        print('6. Borrar Cliente')
        print('7. Regresar')

    #Funcion de Mostrar Datos del Cliente
    def show_a_cliente(self, record):
        print('ID:', record[0])
        print('Nombres:', record[1])
        print('Apellidos:', record[2])
        print('E-mail:', record[3])
        print('Telefono:', record[4])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_cliente_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    #Funcion para separar Diferentes Datos
    def show_cliente_midder(self):
        print('-'*48)

    #Funcion de Terminacion de los Clientes
    def show_cliente_footer(self):
        print('*'*48)

    """
    ***********************
    * Views for Peliculas *
    ***********************
    """

    #Funcion para el Menu de las Peliculas
    def pelicula_menu(self):
        print('***************************')
        print('* -- Submenu Peliculas -- *')
        print('***************************')
        print('1. Agregar Pelicula')
        print('2. Leer Pelicula')
        print('3. Leer todos las Peliculas')
        print('4. Actualizar Pelicula')
        print('5. Borrar Pelicula')
        print('6. Regresar')

    #Funcion de Mostrar Datos de la Pelicula
    def show_a_pelicula(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Genero:', record[2])
        print('Clasificacion:', record[3])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_pelicula_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    #Funcion para separar Diferentes Datos
    def show_pelicula_midder(self):
        print('-'*48)

    #Funcion de Terminacion de los Productos
    def show_pelicula_footer(self):
        print('*'*48)

    """
    ******************
    * Views for Sala *
    ******************
    """

    #Funcion para el Menu de las Salas
    def sala_menu(self):
        print('**********************')
        print('* -- Submenu Sala -- *')
        print('**********************')
        print('1. Agregar Sala')
        print('2. Leer Sala')
        print('3. Leer todos los Sala')
        print('4. Actualizar Sala')
        print('5. Borrar Sala')
        print('6. Regresar')

    #Funcion de Mostrar Datos de la Sala
    def show_a_sala(self, record):
        print('ID:', record[0])
        print('Total de Asientos:', record[1])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_sala_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    #Funcion para separar Diferentes Datos
    def show_sala_midder(self):
        print('-'*48)

    #Funcion de Terminacion de las Salas
    def show_sala_footer(self):
        print('*'*48)

    """
    **********************
    * Views for Asientos *
    **********************
    """

    #Funcion para el Menu de las Asientos
    def asiento_menu(self):
        print('**************************')
        print('* -- Submenu Asientos -- *')
        print('**************************')
        print('1. Agregar Asiento')
        print('2. Leer Asiento')
        print('3. Leer todos los Asientos')
        print('4. Actualizar Asiento')
        print('5. Borrar Asiento')
        print('6. Regresar')

    #Funcion Mostrar Asiento
    """
    El ID del asiento es su numero dentro de una sala de este cine :D
    """
    def show_a_asiento(self, record):
        print('ID:', record[0])
        print('Disponibilidad:', record[1])
        print('Numero de Sala:', record[2])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_asiento_header(self, header):
        print(header.center(30,'*'))
        print('-'*30)

    #Funcion para separar Diferentes Datos
    def show_asiento_midder(self):
        print('-'*30)

    #Funcion de Terminacion de los Asientos
    def show_asiento_footer(self):
        print('*'*30)

    """
    *******************
    * Views for Views *
    *******************
    """
    #Este mostrara los datos sobre pelicula 

    #Funcion para el Menu de los View
    def mostrar_menu(self):
        print('*************************')
        print('* -- Submenu Mostrar -- *')
        print('*************************')
        print('1. Agregar View')
        print('2. Leer View')
        print('3. Leer todos los Views')
        print('4. Actualizar View')
        print('5. Borrar View')
        print('6. Regresar')

    #Funcion Mostrar View
    def show_a_mostrar(self, record):
        print('ID:', record[0])
        print('Fecha de la Pelicula:', record[1])
        print('Duracion:', record[2])
        print('Pelicula:', record[3])
        print('Sala:', record[4])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_mostrar_header(self, header):
        print(header.center(30,'*'))
        print('-'*30)

    #Funcion para separar Diferentes Datos
    def show_mostrar_midder(self):
        print('-'*30)

    #Funcion de Terminacion de los Mostrar
    def show_mostrar_footer(self):
        print('*'*30)

    """
    ********************
    * Views for Compra *
    ********************
    """

    #Funcion para el Menu de las Compra
    def compra_menu(self):
        print('***************************')
        print('* -- Submenu Compras -- *')
        print('***************************')
        print('1. Agregar Compra')
        print('2. Leer Compra')
        print('3. Leer todos las Compras')
        print('4. Actualizar Compra')
        print('5. Borrar Compra')
        print('6. Regresar')

    #Funcion Mostrar Compra
    def show_a_compra(self, record):
        print('ID:', record[0])
        print('Costo Boleto:', record[1])
        print('ID Cliente:', record[2])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_compra_header(self, header):
        print(header.center(30,'*'))
        print('-'*30)

    #Funcion para separar Diferentes Datos
    def show_compra_midder(self):
        print('-'*30)

    #Funcion de Terminacion de los Compra
    def show_compra_footer(self):
        print('*'*30)

    """
    *********************
    * Views for Tickets *
    *********************
    """

    #Funcion para el Menu de los Tickets
    def ticket_menu(self):
        print('***************************')
        print('* -- Submenu Tickets -- *')
        print('***************************')
        print('1. Agregar Ticket')
        print('2. Leer Ticket')
        print('3. Leer todos los Tickets')
        print('4. Actualizar Ticket')
        print('5. Borrar Ticket')
        print('6. Regresar')

    #Funcion Mostrar Ticket
    def show_a_ticket(self, record):
        print('ID:', record[0])
        #print('Costo Boleto:', record[1])
        print('ID Compra:', record[1])
        print('Fecha de la Pelicula:', record[2])
        print('Duracion de la Pelicula:', record[3])
        print('Sala:', record[4])
        print('Asiento:', record[5])
        print('Pelicula:', record[6])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_ticket_header(self, header):
        print(header.center(30,'*'))
        print('-'*30)

    #Funcion para separar Diferentes Datos
    def show_ticket_midder(self):
        print('-'*30)

    #Funcion de Terminacion de los Ticket
    def show_ticket_footer(self):
        print('*'*30)