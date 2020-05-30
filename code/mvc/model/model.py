from mysql import connector

class Model:
    """
    ******************************************************
    * A data model with MySQL for a movie ticket sale DB *
    ******************************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **********************
    * Metodos de Cliente *
    **********************
    """

    #Metodo para Crear Clientes
    def create_cliente(self, c_nombre, c_apelidos, c_email, c_telefono):
        try:
            sql = 'INSERT INTO cliente (`c_nombre`, `c_apellidos`, `c_email`, `c_telefono`) VALUES (%s, %s, %s, %s)'
            vals = (c_nombre, c_apelidos, c_email, c_telefono)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Cliente
    def read_a_cliente(self, id_cliente):
        try:
            sql = 'SELECT * FROM cliente WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los CLientes
    def read_all_clientes(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM cliente'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer a los Clientes por Numero de Telefono
    def read_cliente_telefono(self, c_telefono):
        try:
            sql = 'SELECT * FROM cliente WHERE c_telefono = %s'
            vals = (c_telefono,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Cliente
    def update_cliente(self, fields, vals):
        try:
            sql = 'UPDATE cliente SET '+','.join(fields)+' WHERE id_cliente = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar Cliente
    def delete_cliente(self, id_cliente):
        try:
            sql = 'DELETE FROM cliente WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Pelicula methods *
    ********************
    """

    #Metodo para Crear una Pelicula
    def create_pelicula(self, p_nombre, p_genero, p_clasificacion):
        try:
            sql = 'INSERT INTO pelicula (`p_nombre`, `p_genero`, `p_clasificacion`) VALUES (%s, %s, %s)'
            vals = (p_nombre, p_genero, p_clasificacion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer una Pelicula
    def read_a_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos las Peliculas
    def read_all_peliculas(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar una Pelicula
    def update_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar Pelicula
    def delete_pelicula(self, id_pelicula):
        try:
            sql = 'DELETE FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Sala methods *
    ****************
    """

    #Metodo para Crear una Sala
    def create_sala(self, s_total_asientos):
        try:
            sql = 'INSERT INTO sala (`s_total_asientos`) VALUES (%s)'
            vals = (s_total_asientos)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer una Sala
    def read_a_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todas las Salas
    def read_all_salas(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar una Sala
    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE sala SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar una Sala
    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * Metodos de Asientos *
    ***********************
    """

    #Metodo para Crear Asientos
    def create_asiento(self, a_disponibilidad, id_sala):
        try:
            sql = 'INSERT INTO asiento (`a_disponibilidad`, `id_sala`) VALUES (%s, %s)'
            vals = (a_disponibilidad, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Asiento
    def read_a_asiento(self, id_asiento):
        try:
            sql = 'SELECT asiento.*,sala.id_sala FROM asiento JOIN sala ON asiento.id_sala = sala.id_sala and asiento.id_sala = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Asientos
    def read_all_asientos(self): #Caution with large amount of data
        try:
            sql = 'SELECT asiento.*,sala.id_sala,sala.s_total_asientos FROM asiento JOIN sala ON asiento.id_sala = sala.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Asiento
    def update_asiento(self, fields, vals):
        try:
            sql = 'UPDATE asiento SET '+','.join(fields)+' WHERE id_asiento = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Eliminar un Asiento
    def delete_asiento(self, id_asiento):
        try:
            sql = 'DELETE FROM asiento WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Views methods  *
    ********************
    """

    #Metodo para Crear Views
    def create_view(self, m_fecha_pelicula, m_duracion, m_horario, id_pelicula, id_sala):
        try:
            sql = 'INSERT INTO mostrar (`m_fecha_pelicula`, `m_duracion`, `m_horario`, `id_pelicula`, `id_sala`) VALUES (%s, %s, %s, %s, %s)'
            vals = (m_fecha_pelicula, m_duracion, m_horario, id_pelicula, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un View
    def read_a_view(self, id_mostrar):
        try:
            sql = 'SELECT mostrar.*, pelicula.*, sala.* FROM mostrar JOIN sala ON mostrar.id_sala = sala.id_sala JOIN pelicula ON mostrar.id_pelicula = pelicula.id_pelicula WHERE sala.id_sala = %s'
            vals = (id_mostrar,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Views
    def read_all_views(self): #Caution with large amount of data
        try:
            sql = 'select mostrar.*, pelicula.*, sala.* from mostrar join sala on mostrar.id_sala = sala.id_sala join pelicula on mostrar.id_pelicula = pelicula.id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un View
    def update_view(self, fields, vals):
        try:
            sql = 'UPDATE mostrar SET '+','.join(fields)+' WHERE id_mostrar = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar un View
    def delete_view(self, id_mostrar):
        try:
            sql = 'DELETE FROM mostrar WHERE id_mostrar = %s'
            vals = (id_mostrar,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *******************
    * Compra methods  *
    *******************
    """

    #Metodo para Crear Compras
    def create_compra(self, c_costo, id_cliente):
        try:
            sql = 'INSERT INTO compra (`c_costo`, `id_cliente`) VALUES (%s, %s)'
            vals = (c_costo, id_cliente)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer una Compra
    def read_a_compra(self, id_compra): 
        try:
            sql = 'SELECT compra.*, cliente.* FROM compra JOIN cliente ON compra.id_compra = cliente.id_cliente WHERE compra.id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos las Compras
    def read_all_compra(self): #Caution with large amount of data
        try:
            sql = 'SELECT compra.*, cliente.* FROM compra JOIN cliente ON compra.id_compra = cliente.id_cliente'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar una Compra
    def update_compra(self, fields, vals):
        try:
            sql = 'UPDATE compra SET '+','.join(fields)+' WHERE id_compra = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar una Compra
    def delete_compra(self, id_compra):
        try:
            sql = 'DELETE FROM compra WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *******************
    * Ticket methods  *
    *******************
    """

    #Metodo para Crear Tickets
    def create_ticket(self, t_costo, id_compra, id_mostrar, id_sala, id_asiento,id_pelicula):
        try:
            sql = 'INSERT INTO ticket (`t_costo`, `id_compra`, `id_mostrar`, `id_sala`, `id_asiento`,`id_pelicula`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (t_costo, id_compra, id_mostrar, id_sala, id_asiento, id_pelicula)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un ticket
    def read_a_ticket(self, id_ticket): 
        try:
            sql = 'SELECT ticket.id_ticket, compra.id_compra, mostrar.m_fecha_pelicula, mostrar.m_duracion, sala.id_sala, asiento.id_asiento, pelicula.p_nombre FROM ticket JOIN compra ON ticket.id_compra = compra.id_compra JOIN mostrar ON ticket.id_mostrar = mostrar.id_mostrar JOIN sala ON ticket.id_sala = sala.id_sala JOIN asiento ON ticket.id_asiento = asiento.id_asiento JOIN pelicula ON ticket.id_pelicula = pelicula.id_pelicula WHERE ticket.id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Tickets
    def read_all_tickets(self): #Caution with large amount of data
        try:
            sql = 'SELECT ticket.id_ticket, compra.id_compra, mostrar.m_fecha_pelicula, mostrar.m_duracion, sala.id_sala, asiento.id_asiento, pelicula.p_nombre FROM ticket JOIN compra ON ticket.id_compra = compra.id_compra JOIN mostrar ON ticket.id_mostrar = mostrar.id_mostrar JOIN sala ON ticket.id_sala = sala.id_sala JOIN asiento ON ticket.id_asiento = asiento.id_asiento JOIN pelicula ON ticket.id_pelicula = pelicula.id_pelicula;'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Ticket
    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE ticket SET '+','.join(fields)+' WHERE id_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar un Ticket
    def delete_ticket(self, id_ticket):
        try:
            sql = 'DELETE FROM ticket WHERE id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************************
    * Views metodos para Usuario General *
    **************************************
    """

    #Metodo para ver todas las Peliculas y mostrar su contenido
    def read_all_mostrar_peliculas(self): #Caution with large amount of data
        try:
            sql = 'select mostrar.*, pelicula.p_nombre, pelicula.p_clasificacion from mostrar join pelicula on mostrar.id_pelicula = pelicula.id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err