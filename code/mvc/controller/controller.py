from model.model import Model
from view.view import View
from datetime import date
import time
import os
import sys
import getpass

#Clase Controller
class Controller:
    """
    ************************************************************
    * Controlador para la BD de Venta de Boletos para un Cine  *
    ************************************************************
    """

    #Constructor de la Clase
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Metodo para Inicializar todo el Proceso (Sistema)
    def start(self):
        self.view.start()
        self.entrada()
        #self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """
    #Funcion Entrada
    def entrada(self):
        """
        *******************
        * Menu de Entrada *
        *******************
        """
        o = '0'
        while o != '3':
            print('1. Usuarios Generales')
            print('2. Usuarios Administradores')
            print('3. Salir')
            o = input()
            if o == '1':
                self.usuarios_generales()
            elif o == '2':
                usuario = input('User: ')
                passw = getpass.getpass('Password: ')

                if self.login(usuario, passw) == 1:
                    print('Bienvenido ', usuario)
                    self.main_menu()
                else:
                    print('ERROR!! User is not registered.')
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    #Funcion para los Usuarios Generales
    def usuarios_generales(self):
        print('\n\tHola Cliente\n\n')
        print('En este apartado podras ver las peliculas que esten disponibles.\n')
        print('\n\n')
        self.read_all_clientes_peliculas()

        return

    #Metodo para la Lectura de todos las Peliculas para los Clientes
    def read_all_clientes_peliculas(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Todos las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    #Funcion Login
    #Esto sirve solo para los usuarios del cine 
    #Usuarios Administradores
    def login(self,usuario, passw):
        registeredUser = ('admin')
        registeredPW = ('pass')
        if usuario in registeredUser:
            if passw in registeredPW:
                return 1
            else:
                print("\n\tLa contraseña es incorrecta...\n")
        else:
            return 2

    #Funcion del Menu
    def main_menu(self):
        o = '0'
        while o != '8':
            self.view.main_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.cliente_of_menu()
            elif o == '2':
                self.pelicula_of_menu()
            elif o == '3':
                self.sala_of_menu()
            elif o == '4':
                self.asiento_of_menu()
            elif o == '5':
                self.mostrar_of_menu()
            elif o == '6':
                self.compra_of_menu()
            elif o == '7':
                self.ticket_of_menu()
            elif o == '8':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    #Medoto para Generar unas Listas para Cuando Necesitemos Llamar los Metodos de Actualizacion
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals
    
    """
    ****************************
    * Controllers for Clientes *
    ****************************
    """

    #Funcion del Menu de Autores
    def cliente_of_menu(self):
        o = '0'
        while o != '8':
            self.view.cliente_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_cliente()
            elif o == '2':
                self.read_a_cliente()
            elif o == '3':
                self.read_all_clientes()
            elif o == '4':
                self.read_cliente_telefono()
            elif o == '5':
                self.update_cliente()
            elif o == '6':
                self.delete_cliente()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Clientes
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Cliente
    def ask_cliente(self):
        self.view.ask('Nombres: ')
        c_nombre = input()
        self.view.ask('Apellidos: ')
        c_apellidos = input()
        self.view.ask('E-mail: ')
        c_email = input()
        self.view.ask('telefono: ')
        c_telefono = input()
        return [c_nombre, c_apellidos, c_email, c_telefono]

    #Metodo para Crear un Cliente
    def create_cliente(self):
        c_nombre, c_apellidos, c_email, c_telefono = self.ask_cliente()
        out = self.model.create_cliente(c_nombre, c_apellidos, c_email, c_telefono)
        if out == True:
            self.view.ok(c_nombre+' '+c_apellidos, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CLIENTE. REVISA.')
        return

    #Metodo para Leer un Cliente
    def read_a_cliente(self):
        self.view.ask('ID cliente: ')
        id_cliente = input()
        cliente = self.model.read_a_cliente(id_cliente)
        if type(cliente) == tuple:
            self.view.show_cliente_header(' Datos del cliente '+id_cliente+' ')
            self.view.show_a_cliente(cliente)
            self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            if cliente == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA.')
        return

    #Metodo para la Lectura de todos los Clientes
    def read_all_clientes(self):
        clientes = self.model.read_all_clientes()
        if type(clientes) == list:
            self.view.show_cliente_header(' Todos los clientes ')
            for cliente in clientes:
                self.view.show_a_cliente(cliente)
                self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA.')
        return

    #Metodo para Leer los Autores por Telefono
    def read_cliente_telefono(self):
        self.view.ask('Telefono: ')
        telefono = input()
        clientes = self.model.read_cliente_telefono(telefono)
        if type(clientes) == list:
            self.view.show_cliente_header(' Cliente con el telefono '+telefono+' ')
            for cliente in clientes:
                self.view.show_a_cliente(cliente)
                self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA.')
        return

    #Metodo para Actualizar los Clientes
    def update_cliente(self):
        self.view.ask('ID del cliente a modificar: ')
        id_cliente = input()
        cliente = self.model.read_a_cliente(id_cliente)
        if type(cliente) == tuple:
            self.view.show_cliente_header(' Datos del cliente '+id_cliente+' ')
            self.view.show_a_cliente(cliente)
            self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            if cliente == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL CLIENTE. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_cliente()
        fields, vals = self.update_lists(['c_nombre','c_apellidos','c_email','c_telefono'], whole_vals)
        vals.append(id_cliente)
        vals = tuple(vals)
        out = self.model.update_cliente(fields, vals)
        if out == True:
            self.view.ok(id_cliente, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR AL CLIENTE. REVISA.')
        return

    #Metodo para Borrar el Cliente
    def delete_cliente(self):
        self.view.ask('ID del cliente a borrar: ')
        id_cliente = input()
        count = self.model.delete_cliente(id_cliente)
        if count != 0:
            self.view.ok(id_cliente, 'borro')
        else:
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CLIENTE. REVISA.')
        return

    """
    *****************************
    * Controllers for Peliculas *
    *****************************
    """

    #Funcion del Menu de Peliculas
    def pelicula_of_menu(self):
        o = '0'
        while o != '8':
            self.view.pelicula_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_pelicula()
            elif o == '2':
                self.read_a_pelicula()
            elif o == '3':
                self.read_all_pelicula()
            elif o == '4':
                self.update_pelicula()
            elif o == '5':
                self.delete_pelicula()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Peliculas
    #Esto le pide al Usuario Ingresar los Datos Requeridos para una Pelicula
    def ask_pelicula(self):
        self.view.ask('Nombre Pelicula: ')
        p_nombre = input()
        self.view.ask('Genero: ')
        p_genero = input()
        self.view.ask('Clasificacion: ')
        p_clasificacion = input()
        return [p_nombre, p_genero, p_clasificacion]

    #Metodo para Crear una Pelicula
    def create_pelicula(self):
        p_nombre, p_genero, p_clasificacion = self.ask_pelicula()
        out = self.model.create_pelicula(p_nombre, p_genero, p_clasificacion)
        if out == True:
            self.view.ok(p_nombre+' '+p_clasificacion, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return

    #Metodo para Leer una Pelicula
    def read_a_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('EL PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return

    #Metodo para la Lectura de todos las Peliculas
    def read_all_pelicula(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Todos las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    #Metodo para Actualizar las Peliculas
    def update_pelicula(self):
        self.view.ask('ID de la pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['p_nombre','p_genero','p_clasificacion'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields, vals)
        if out == True:
            self.view.ok(id_pelicula, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA.')
        return

    #Metodo para Borrar la Pelicula
    def delete_pelicula(self):
        self.view.ask('ID de la pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_pelicula(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return

    """
    ************************
    * Controllers for Sala *
    ************************
    """

    #Funcion del Menu de Sala
    def sala_of_menu(self):
        o = '0'
        while o != '6':
            self.view.sala_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_sala()
            elif o == '4':
                self.update_sala()
            elif o == '5':
                self.delete_sala()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Salas de Cine
    #Esto le pide al Usuario Ingresar los Datos Requeridos para una Sala
    def ask_sala(self):
        self.view.ask('Total de Asientos: ')
        s_total_asientos = int(input())
        return [s_total_asientos]

    #Metodo para Crear una Sala
    def create_sala(self):
        s_total_asientos = self.ask_sala()
        out = self.model.create_sala(s_total_asientos)
        if out == True:
            self.view.ok(s_total_asientos, ' agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA.')
        return

    #Metodo para Leer una Sala
    def read_a_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        return

    #Metodo para la Lectura de todos las Salas
    def read_all_sala(self):
        salas = self.model.read_all_salas()
        if type(salas) == list:
            self.view.show_sala_header(' Todas las salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA.')
        return

    #Metodo para Actualizar las Salas
    def update_sala(self):
        self.view.ask('ID de la sala a modificar: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['s_total_asientos'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(id_sala, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA.')
        return

    #Metodo para Borrar la Sala
    def delete_sala(self):
        self.view.ask('ID de la sala a borrar: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala, 'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA.')
        return

    """
    ***************************
    * Controllers for Asiento *
    ***************************
    """

    #Funcion del Menu para los Asientos
    def asiento_of_menu(self):
        o = '0'
        while o != '6':
            self.view.asiento_menu()
            self.view.option('7')
            o = input()
            if o =='1':
                self.create_asiento()
            elif o == '2':
                self.read_a_asiento()
            elif o == '3':
                self.read_all_asientos()
            elif o == '4':
                self.update_asiento()
            elif o == '5':
                self.delete_asiento()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Asientos
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Asiento
    def ask_asiento(self):
        self.view.ask('Disponibilidad: ')
        a_disponibilidad = input()
        self.view.ask('Sala (Solo ID): ')
        sala = input()
        return [a_disponibilidad,sala]

    #Metodo para Crear un Asiento
    def create_asiento(self):
        a_disponibilidad, sala = self.ask_asiento()
        out = self.model.create_asiento(a_disponibilidad, sala)
        if out == True:
            self.view.ok(a_disponibilidad+' '+sala, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return

    #Metodo para Leer un Asiento
    def read_a_asiento(self):
        self.view.ask('ID asiento: ')
        id_asiento = input()
        asiento = self.model.read_a_asiento(id_asiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos del Asiento '+id_asiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return

    #Metodo para Leer todos los Asiento
    def read_all_asientos(self):
        asientos = self.model.read_all_asientos()
        if type(asientos) == list:
            self.view.show_asiento_header(' Todos los asientos ')
            for asiento in asientos:
                self.view.show_a_asiento(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA.')
        return

    #Metodo para Actualizar un Asiento
    def update_asiento(self):
        self.view.ask('ID del asiento a modificar: ')
        id_asiento = input()
        asiento = self.model.read_a_asiento(id_asiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos del asiento '+id_asiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_asiento()
        fields, vals = self.update_lists(['a_disponibilidad','id_sala'], whole_vals)
        vals.append(id_asiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields, vals)
        if out == True:
            self.view.ok(id_asiento, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO. REVISA.')
        return

    #Metodo para Borrar un Asiento
    def delete_asiento(self):
        self.view.ask('ID del asiento a borrar:')
        id_asiento = input()
        count = self.model.delete_asiento(id_asiento)
        if count != 0:
            self.view.ok(id_asiento, 'borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISA.')
        return

    """
    *************************
    * Controllers for Views *
    *************************
    """

    #Funcion del Menu para Mostrar
    def mostrar_of_menu(self):
        o = '0'
        while o != '6':
            self.view.mostrar_menu()
            self.view.option('6')
            o = input()
            if o =='1':
                self.create_view()
            elif o == '2':
                self.read_a_view()
            elif o == '3':
                self.read_all_view()
            elif o == '4':
                self.update_view()
            elif o == '5':
                self.delete_view()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Views
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Views
    def ask_view(self):
        self.view.ask('Fecha Pelicula: ')
        m_fecha_pelicula = input()
        self.view.ask('Duracion: ')
        m_duracion = input()
        self.view.ask('Horario: ')
        m_horario = input()
        self.view.ask('Pelicula (Solo ID): ')
        pelicula = input()
        self.view.ask('Sala (Solo ID): ')
        sala = input()
        return [m_fecha_pelicula,m_duracion,m_horario,pelicula,sala]

    #Metodo para Crear un View
    def create_view(self):
        m_fecha_pelicula,m_duracion, m_horario, pelicula, sala = self.ask_view()
        out = self.model.create_view(m_fecha_pelicula, m_duracion, m_horario, pelicula, sala)
        if out == True:
            self.view.ok(m_horario, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL VIEW. REVISA.')
        return

    #Metodo para Leer un View
    def read_a_view(self):
        self.view.ask('ID mostrar: ')
        id_mostrar = input()
        mostrar = self.model.read_a_view(id_mostrar)
        if type(mostrar) == tuple:
            self.view.show_mostrar_header(' Datos del view '+id_mostrar+' ')
            self.view.show_a_mostrar(mostrar)
            self.view.show_mostrar_midder()
            self.view.show_mostrar_footer()
        else:
            if mostrar == None:
                self.view.error('EL VIEW NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL VIEW. REVISA.')
        return

    #Metodo para Leer todos los View
    def read_all_view(self):
        views = self.model.read_all_views()
        if type(views) == list:
            self.view.show_mostrar_header(' Todos los views ')
            for view in views:
                self.view.show_a_mostrar(view)
                self.view.show_mostrar_midder()
            self.view.show_mostrar_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS VIEW. REVISA.')
        return

    #Metodo para Actualizar un View
    def update_view(self):
        self.view.ask('ID del view a modificar: ')
        id_mostrar = input()
        mostrar = self.model.read_a_view(id_mostrar)
        if type(mostrar) == tuple:
            self.view.show_mostrar_header(' Datos del view '+id_mostrar+' ')
            self.view.show_a_mostrar(mostrar)
            self.view.show_mostrar_midder()
            self.view.show_mostrar_footer()
        else:
            if mostrar == None:
                self.view.error('EL VIEW NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL VIEW. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_view()
        fields, vals = self.update_lists(['m_fecha_pelicula','m_duracion', 'm_horario','id_pelicula', 'id_sala'], whole_vals)
        vals.append(id_mostrar)
        vals = tuple(vals)
        out = self.model.update_view(fields, vals)
        if out == True:
            self.view.ok(id_mostrar, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL VIEW. REVISA.')
        return

    #Metodo para Borrar un View
    def delete_view(self):
        self.view.ask('ID del view a borrar:')
        id_mostrar = input()
        count = self.model.delete_view(id_mostrar)
        if count != 0:
            self.view.ok(id_mostrar, 'borro')
        else:
            if count == 0:
                self.view.error('EL VIEW NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL VIEW. REVISA.')
        return

    """
    **************************
    * Controllers for Compra *
    **************************
    """

    #Funcion del Menu para las Compras
    def compra_of_menu(self):
        o = '0'
        while o != '6':
            self.view.compra_menu()
            self.view.option('6')
            o = input()
            if o =='1':
                self.create_compra()
            elif o == '2':
                self.read_a_compra()
            elif o == '3':
                self.read_all_compra()
            elif o == '4':
                self.update_compra()
            elif o == '5':
                self.delete_compra()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Compras
    #Esto le pide al Usuario Ingresar los Datos Requeridos para una Compra
    def ask_compra(self):
        self.view.ask('Costo Boleto: ')
        c_costo = input()
        self.view.ask('Usuario (Solo ID): ')
        usuario = input()
        return [c_costo,usuario]

    #Metodo para Crear una Compra
    def create_compra(self):
        c_costo, usuario = self.ask_compra()
        out = self.model.create_compra(c_costo, usuario)
        if out == True:
            self.view.ok(c_costo+' '+usuario, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA COMPRA. REVISA.')
        return

    #Metodo para Leer una Compra
    def read_a_compra(self):
        self.view.ask('ID compra: ')
        id_compra = input()
        compra = self.model.read_a_compra(id_compra)
        if type(compra) == tuple:
            self.view.show_compra_header(' Datos de la compra '+id_compra+' ')
            self.view.show_a_compra(compra)
            self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            if compra == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        return

    #Metodo para Leer todas las Compras
    def read_all_compra(self):
        compras = self.model.read_all_compra()
        if type(compras) == list:
            self.view.show_compra_header(' Todas las compras ')
            for compra in compras:
                self.view.show_a_compra(compra)
                self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS COMPRAS. REVISA.')
        return

    #Metodo para Actualizar una Compra
    def update_compra(self):
        self.view.ask('ID de la compra a modificar: ')
        id_compra = input()
        compra = self.model.read_a_compra(id_compra)
        if type(compra) == tuple:
            self.view.show_compra_header(' Datos de la compra '+id_compra+' ')
            self.view.show_a_compra(compra)
            self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            if compra == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_compra()
        fields, vals = self.update_lists(['c_costo','id_cliente'], whole_vals)
        vals.append(id_compra)
        vals = tuple(vals)
        out = self.model.update_compra(fields, vals)
        if out == True:
            self.view.ok(id_compra, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA COMPRA. REVISA.')
        return

    #Metodo para Borrar una Compra
    def delete_compra(self):
        self.view.ask('ID de la compra a borrar:')
        id_compra = input()
        count = self.model.delete_compra(id_compra)
        if count != 0:
            self.view.ok(id_compra, 'borro')
        else:
            if count == 0:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA COMPRA. REVISA.')
        return

    """
    ***************************
    * Controllers for Tickets *
    ***************************
    """

    #Funcion del Menu para los Libros
    def ticket_of_menu(self):
        o = '0'
        while o != '6':
            self.view.ticket_menu()
            self.view.option('6')
            o = input()
            if o =='1':
                self.create_ticket()
            elif o == '2':
                self.read_a_ticket()
            elif o == '3':
                self.read_all_tickets()
            elif o == '4':
                self.update_ticket()
            elif o == '5':
                self.delete_ticket()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Tickets
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Ticket
    def ask_ticket(self):
        self.view.ask('Costo Boleto: ')
        t_costo = input()
        self.view.ask('Compra (Solo ID): ')
        compra = input()
        self.view.ask('View (Solo ID): ')
        view = input()
        self.view.ask('Sala (Solo ID): ')
        sala = input()
        self.view.ask('Asiento (Solo ID): ')
        asiento = input()
        self.view.ask('Pelicula (Solo ID): ')
        pelicula = input()
        return [t_costo,compra,view,sala,asiento,pelicula]

    #Metodo para Crear un Ticket
    def create_ticket(self):
        t_costo, compra, view, sala, asiento, pelicula = self.ask_ticket()
        out = self.model.create_ticket(t_costo, compra, view, sala, asiento, pelicula)
        if out == True:
            self.view.ok(t_costo, 'agrego')#POSIBLE FALLO
        else:
            self.view.error('NO SE PUDO AGREGAR EL TICKET. REVISA.')
        return

    #Metodo para Leer un Ticket
    def read_a_ticket(self):
        self.view.ask('ID ticket: ')
        id_ticket = input()
        ticket = self.model.read_a_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+id_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL TICKET. REVISA.')
        return

    #Metodo para Leer todos los Tickets
    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if type(tickets) == list:
            self.view.show_ticket_header(' Todos los tickets ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS TICKETS. REVISA.')
        return

    #Metodo para Actualizar un Ticket
    def update_ticket(self):
        self.view.ask('ID del ticket a modificar: ')
        id_ticket = input()
        ticket = self.model.read_a_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+id_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL TICKET. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_ticket()
        fields, vals = self.update_lists(['t_costo', 'id_compra', 'id_mostrar', 'id_sala', 'id_asiento','id_pelicula'], whole_vals)
        vals.append(id_ticket)
        vals = tuple(vals)
        out = self.model.update_ticket(fields, vals)
        if out == True:
            self.view.ok(id_ticket, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL TICKET. REVISA.')
        return

    #Metodo para Borrar un Ticket
    def delete_ticket(self):
        self.view.ask('ID del ticket a borrar:')
        id_ticket = input()
        count = self.model.delete_ticket(id_ticket)
        if count != 0:
            self.view.ok(id_ticket, 'borro')
        else:
            if count == 0:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL TICKET. REVISA.')
        return

    