from tkinter import ttk

class PaginaBase(ttk.Frame):
    """
    Clase base con la estructura comun de titulo y subtitulo para las vistas
    """

    titulo = "Página"
    subtitulo = ""

    def __init__(self, contenedor):
        super().__init__(contenedor, style="Contenido.TFrame")
        self._armar_encabezado()
        self.construir_contenido()

    def _armar_encabezado(self):
        ttk.Label(
            self, text=self.titulo, style="TituloPagina.TLabel"
        ).pack(anchor="w", padx=24, pady=(20, 2))

        if self.subtitulo:
            ttk.Label(
                self, text=self.subtitulo, style="Subtitulo.TLabel"
            ).pack(anchor="w", padx=24, pady=(0, 16))

    def construir_contenido(self):
        """
        Método para sobreescribir en cada subclase con formularios o tablas
        """
        ttk.Label(
            self,
            text="¡Bienvenido al sistema de PeluCan!",
            style="Placeholder.TLabel",
        ).pack(anchor="w", padx=24, pady=10)


#Subclases especificas para cada seccion del sistema
class PaginaInicio(PaginaBase):
    titulo = "Inicio – Panel General"
    subtitulo = "Resumen de actividad y próximos turnos programados."

    def construir_contenido(self):
        # Marco para tarjetas de métricas / resumen
        frame_metricas = ttk.Frame(self, style="Contenido.TFrame")
        frame_metricas.pack(fill="x", padx=24, pady=(0, 15))

        # Tarjetas de resumen (Turnos, Clientes, Mascotas)
        tarjetas = [
            ("TURNOS DEL DÍA", "8"),
            ("CLIENTES REGISTRADOS", "124"),
            ("MASCOTAS REGISTRADAS", "87"),
        ]

        for titulo, valor in tarjetas:
            card = ttk.LabelFrame(frame_metricas, text=titulo, padding=(15, 10))
            card.pack(side="left", fill="both", expand=True, padx=5)
            ttk.Label(card, text=valor, font=("Segoe UI", 18, "bold")).pack()

        # Título de la tabla
        ttk.Label(
            self, text="Próximos turnos del día", font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", padx=24, pady=(10, 5))

        # Tabla de próximos turnos
        columnas = ("mascota", "servicio", "fecha", "hora", "estado")
        tabla = ttk.Treeview(self, columns=columnas, show="headings", height=6)
        
        tabla.heading("mascota", text="Mascota")
        tabla.heading("servicio", text="Servicio")
        tabla.heading("fecha", text="Fecha")
        tabla.heading("hora", text="Hora")
        tabla.heading("estado", text="Estado")

        # Datos de ejemplo
        datos_ejemplo = [
            ("Luna (Caniche)", "Baño completo", "31/08/2026", "09:00", "Pendiente"),
            ("Bruno (Labrador)", "Corte + Baño", "31/08/2026", "10:30", "Confirmado"),
            ("Toby (Cocker)", "Corte de uñas", "31/08/2026", "11:45", "Confirmado"),
            ("Coco (Golden)", "Baño completo", "31/08/2026", "14:00", "Pendiente"),
            ("Lola (Beagle)", "Desparasitado", "31/08/2026", "16:30", "Completado"),
        ]

        for fila in datos_ejemplo:
            tabla.insert("", "end", values=fila)

        tabla.pack(fill="both", expand=True, padx=24, pady=(0, 20))


class PaginaClientes(PaginaBase):
    titulo = "Listado de Clientes"
    subtitulo = "Administración y búsqueda de clientes registrados en el sistema."


class PaginaMascotas(PaginaBase):
    titulo = "Listado de Mascotas"
    subtitulo = "Administración y búsqueda general de mascotas registradas."


class PaginaTurnos(PaginaBase):
    titulo = "Listado de Turnos"
    subtitulo = "Administración y búsqueda general de citas programadas en el sistema."


class PaginaServicios(PaginaBase):
    titulo = "Servicios"
    subtitulo = "Servicios ofrecidos por la peluquería."
