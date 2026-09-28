CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL UNIQUE,
    correo VARCHAR(100) UNIQUE
);

CREATE TABLE mascota (
    mascota_id SERIAL PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    raza VARCHAR(60),
    edad SMALLINT CHECK (edad >= 0),
    tamano VARCHAR(10) NOT NULL DEFAULT 'Mediano',
    observaciones TEXT,
    id_cliente INTEGER NOT NULL,
    CONSTRAINT fk_mascota_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente) ON DELETE CASCADE
 );

    CREATE TABLE PELUQUERO (
    id_peluquero SERIAL PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    especialidad VARCHAR(50)
 );
     CREATE TABLE SERVICIO (
    id_servicio SERIAL PRIMARY KEY,
    nombre_servicio VARCHAR(80) NOT NULL UNIQUE,
    duracion_estimada INT NOT NULL CHECK (duracion_estimada > 0),
    precio_base NUMERIC(10,2) NOT NULL CHECK (precio_base >= 0)
);
    CONSTRAINT chk_tamano
        CHECK (tamano IN ('Pequeño', 'Mediano', 'Grande')),

    CONSTRAINT fk_mascota_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);

CREATE TABLE turno (
    id_turno SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
    id_mascota INTEGER NOT NULL,

    CONSTRAINT chk_estado_turno
        CHECK (
            estado IN (
                'Pendiente',
                'Confirmado',
                'Completado',
                'Cancelado'
            )
        ),

    CONSTRAINT fk_turno_mascota
        FOREIGN KEY (id_mascota)
        REFERENCES mascota(mascota_id)
    CONSTRAINT fk_turno_peluquero 
        FOREIGN KEY (id_peluquero) 
        REFERENCES PELUQUERO(id_peluquero),
    CONSTRAINT fk_turno_servicio 
        FOREIGN KEY (id_servicio) 
        REFERENCES SERVICIO(id_servicio),

    CONSTRAINT unq_mascota_fecha_hora UNIQUE (id_mascota, fecha, hora),
    CONSTRAINT unq_peluquero_fecha_hora UNIQUE (id_peluquero, fecha, hora)
);

    CREATE TABLE PAGO (
        id_pago SERIAL PRIMARY KEY,
        monto NUMERIC(10,2) NOT NULL CHECK (monto > 0),
        fecha_pago TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        metodo_pago VARCHAR(30) NOT NULL CHECK (metodo_pago IN ('Efectivo', 'Transferencia', 'Tarjeta')),
        id_turno INT NOT NULL UNIQUE,
        CONSTRAINT fk_pago_turno FOREIGN KEY (id_turno) REFERENCES TURNO(id_turno)

);
