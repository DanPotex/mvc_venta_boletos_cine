CREATE DATABASE IF NOT EXISTS venta_boletos;

USE venta_boletos;

CREATE TABLE IF NOT EXISTS cliente
(
	id_cliente INT NOT NULL AUTO_INCREMENT,
    c_nombre VARCHAR(30) NOT NULL,
    c_apellidos VARCHAR(30) NOT NULL,
    c_email VARCHAR(40) NOT NULL,
    c_telefono VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_cliente)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS pelicula
(
	id_pelicula INT NOT NULL AUTO_INCREMENT,
    p_nombre VARCHAR(20) NOT NULL,
    p_genero VARCHAR(20) NOT NULL,
    p_clasificacion VARCHAR(3) NOT NULL,
    PRIMARY KEY (id_pelicula)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS sala
(
	id_sala INT NOT NULL AUTO_INCREMENT,
    s_total_asientos INT NOT NULL,
    PRIMARY KEY (id_sala)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS asiento
(
	id_asiento INT NOT NULL AUTO_INCREMENT,
    a_disponibilidad VARCHAR(2) NOT NULL,
    id_sala INT,
    PRIMARY KEY (id_asiento),
    CONSTRAINT fk_id_sala FOREIGN KEY (id_sala)
		REFERENCES sala(id_sala)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS mostrar
(
	id_mostrar INT NOT NULL AUTO_INCREMENT,
    m_fecha_pelicula DATE NOT NULL,
    m_duracion VARCHAR(8) NOT NULL,
    m_horario VARCHAR(8) NOT NULL,
    id_pelicula INT,
    id_sala INT,
    PRIMARY KEY (id_mostrar),
    CONSTRAINT fk_id_pelicula FOREIGN KEY (id_pelicula)
		REFERENCES pelicula(id_pelicula)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_idsala FOREIGN KEY (id_sala)
		REFERENCES sala(id_sala)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF  NOT EXISTS compra
(
	id_compra INT NOT NULL AUTO_INCREMENT,
    #c_total_tickets INT NOT NULL,
    c_costo FLOAT NOT NULL,
    id_cliente INT,
    PRIMARY KEY (id_compra),
    CONSTRAINT fk_id_cliente FOREIGN KEY (id_cliente)
		REFERENCES cliente(id_cliente)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS ticket
(
	id_ticket INT NOT NULL AUTO_INCREMENT,
    t_costo FLOAT NOT NULL,
    id_compra INT,
    id_mostrar INT,
    id_sala INT,
    id_asiento INT,
    id_pelicula INT,
    PRIMARY KEY (id_ticket),
    CONSTRAINT fk_id_compra FOREIGN KEY (id_compra)
		REFERENCES compra(id_compra)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fk_id_mostrar FOREIGN KEY (id_mostrar)
		REFERENCES mostrar(id_mostrar)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fkid_sala FOREIGN KEY (id_sala)
		REFERENCES sala(id_sala)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fkid_asiento FOREIGN KEY (id_asiento)
		REFERENCES asiento(id_asiento)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fkid_pelicula FOREIGN KEY (id_pelicula)
		REFERENCES pelicula(id_pelicula)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;





#select mostrar.*, pelicula.*, sala.* from mostrar join sala on mostrar.id_sala = sala.id_sala join pelicula on mostrar.id_pelicula = pelicula.id_pelicula where sala.id_sala = 1;

