from datos.conexion import obtener_conexion


def listar():
    """Devuelve todas las mascotas con el nombre de su dueño (lista de tuplas)."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("""SELECT m.id_mascota, m.nombre, COALESCE(m.raza, ''), COALESCE(m.edad::text, ''),
                                 m.tamano, COALESCE(m.observaciones, ''), c.nombre || ' ' || c.apellido
                          FROM mascota m
                          JOIN cliente c ON m.id_cliente = c.id_cliente
                          ORDER BY m.id_mascota""")
        filas = cursor.fetchall()
        cursor.close()
    finally:
        conexion.close()
    return filas