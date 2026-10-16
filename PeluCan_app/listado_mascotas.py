# pyright: reportOptionalMemberAccess=false
from tkinter import messagebox, ttk
from interfaz.paginas.base import PaginaABM
from interfaz.paginas.clientes import CLIENTES_EJEMPLO, etiqueta_cliente
try:
    import psycopg2
    from datos import mascota_dao
except ImportError:
    mascota_dao = None

MASCOTAS_EJEMPLO = [
    {"nombre": "Luna", "raza": "Caniche", "edad": "3", "tamano": "Pequeño", "dueno": "Carlos Gómez", "observaciones": "Ninguna"},
    {"nombre": "Bruno", "raza": "Labrador", "edad": "5", "tamano": "Grande", "dueno": "Ana Ferreyra", "observaciones": "Piel sensible"},
    {"nombre": "Toby", "raza": "Cocker", "edad": "2", "tamano": "Mediano", "dueno": "Marcos Díaz", "observaciones": "Enojo fácil"},
    {"nombre": "Milo", "raza": "Beagle", "edad": "4", "tamano": "Mediano", "dueno": "Lucía Romero", "observaciones": "Muy inquieto"},
    {"nombre": "Simón", "raza": "Bulldog Francés", "edad": "1", "tamano": "Pequeño", "dueno": "Martín Sosa", "observaciones": "Problemas respiratorios leves"},
    {"nombre": "Kira", "raza": "Ovejero Alemán", "edad": "6", "tamano": "Grande", "dueno": "Valeria Benítez", "observaciones": "Muy dócil"},
    {"nombre": "Rocco", "raza": "Boxer", "edad": "3", "tamano": "Grande", "dueno": "Esteban Torres", "observaciones": "Alérgico a perfumes fuertes"},
    {"nombre": "Lola", "raza": "Golden Retriever", "edad": "2", "tamano": "Grande", "dueno": "Camila Navarro", "observaciones": "Cuidado con nudos en las orejas"},
    {"nombre": "Bobi", "raza": "Mestizo", "edad": "7", "tamano": "Mediano", "dueno": "Federico Castro", "observaciones": "Asustadizo con el secador"},
    {"nombre": "Mia", "raza": "Shih Tzu", "edad": "4", "tamano": "Pequeño", "dueno": "Mariana Herrera", "observaciones": "Requiere desenredo suave"},
    {"nombre": "Thor", "raza": "Rottweiler", "edad": "5", "tamano": "Grande", "dueno": "Gonzalo Paz", "observaciones": "Usar bozal preventivo"},
    {"nombre": "Bella", "raza": "Pug", "edad": "3", "tamano": "Pequeño", "dueno": "Florencia Medina", "observaciones": "Limpieza especial de pliegues"},
    {"nombre": "Zeus", "raza": "Husky Siberiano", "edad": "4", "tamano": "Grande", "dueno": "Agustín Vega", "observaciones": "Mucha muda de pelo"},
    {"nombre": "Ciro", "raza": "Dachshund", "edad": "2", "tamano": "Pequeño", "dueno": "Sofía Ríos", "observaciones": "Cuidar la columna al alzar"},
    {"nombre": "Nina", "raza": "Schnauzer Mini", "edad": "3", "tamano": "Pequeño", "dueno": "Joaquín Molina", "observaciones": "Corte de raza tradicional"},
]

def etiqueta_mascota(mascota):
    """Texto con el que se muestra una mascota en los desplegables."""
    return f"{mascota['nombre']} ({mascota['raza']})"

class PaginaMascotas(PaginaABM):
    titulo = "Listado de Mascotas"
    subtitulo = "Administración y búsqueda general de mascotas registradas."
    columnas = [
        ("nombre", "Nombre"),
        ("raza", "Raza"),
        ("edad", "Edad"),
        ("tamano", "Tamaño"),
        ("dueno", "Dueño/a"),
        ("observaciones", "Observaciones"),
    ]
    datos_iniciales = MASCOTAS_EJEMPLO
    campo_busqueda = "nombre"

    opciones_desplegables = {
        "tamano": ["Pequeño", "Mediano", "Grande"],
        "dueno": lambda: [etiqueta_cliente(c) for c in CLIENTES_EJEMPLO],
    }
    
    usa_base = False  # True cuando los datos vienen de PostgreSQL; False = datos de ejemplo en memoria

    def _cargar_datos(self):
        """Lee las mascotas de la base. Si no hay conexión, usa las de ejemplo."""
        if mascota_dao is not None:
            try:
                filas = mascota_dao.listar()
            except psycopg2.Error:
                filas = None
            if filas is not None:
                claves = ("id", "nombre", "raza", "edad", "tamano", "observaciones", "dueno")
                self.datos = [dict(zip(claves, fila)) for fila in filas]
                self.usa_base = True
                return
        self.datos = self.datos_iniciales
        self.usa_base = False

    def _mostrar_estado_conexion(self):
        """Cartelito que avisa de dónde salen los datos."""
        if not hasattr(self, "lbl_estado"):
            self.lbl_estado = ttk.Label(self.marco_listado, style="Subtitulo.TLabel")
            self.lbl_estado.pack(anchor="w", padx=24, pady=(0, 6), before=self.marco_listado.winfo_children()[0])
        self.lbl_estado.configure(
            text="● Conectado a la base de datos PostgreSQL (solo lectura)."
            if self.usa_base
            else "● Sin conexión a la base: se muestran datos de ejemplo y los cambios no se guardan."
        )

    def _refrescar_listado(self):
        self._cargar_datos()
        self._mostrar_estado_conexion()
        super()._refrescar_listado()

    def _al_presionar_guardar(self):
        if self.usa_base:
            messagebox.showinfo("Solo lectura", "Por ahora el listado de mascotas se lee de la base. Alta y edición: próximamente.")
            return
        super()._al_presionar_guardar()

    def _al_presionar_eliminar(self):
        if self.usa_base:
            messagebox.showinfo("Solo lectura", "Por ahora el listado de mascotas se lee de la base. La baja: próximamente.")
            return
        seleccion = self.tabla.selection()
        if seleccion:
            from