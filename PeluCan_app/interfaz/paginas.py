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

    def construir_contenido(self):
        # Barra superior con buscador y botones
        frame_top = ttk.Frame(self, style="Contenido.TFrame")
        frame_top.pack(fill="x", padx=24, pady=(0, 10))

        ttk.Entry(frame_top, width=35).pack(side="left", padx=(0, 10))
        ttk.Button(frame_top, text="Buscar").pack(side="left")

        ttk.Button(frame_top, text="Eliminar").pack(side="right", padx=2)
        ttk.Button(frame_top, text="Editar").pack(side="right", padx=2)
        ttk.Button(frame_top, text="Nuevo", command=self.abrir_formulario_cliente).pack(side="right", padx=2)

        # Tabla de Clientes
        columnas = ("nombre", "telefono", "email", "mascotas")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)

        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("email", text="Email")
        self.tabla.heading("mascotas", text="Mascotas")

        datos_ejemplo = [
            ("Carlos Gómez", "351-555-0110", "carlos.gomez@mail.com", "1"),
            ("Ana Ferreyra", "351-555-0142", "ana.ferreyra@mail.com", "2"),
            ("Marcos Díaz", "351-555-0198", "marcos.diaz@mail.com", "1"),
            ("Lucía Vera", "351-555-0121", "lucia.vera@mail.com", "3"),
        ]

        for fila in datos_ejemplo:
            self.tabla.insert("", "end", values=fila)

        self.tabla.pack(fill="both", expand=True, padx=24, pady=(0, 20))

    def abrir_formulario_cliente(self):
        """Ventana modal con el formulario de Alta de Cliente"""
        top = tk.Toplevel(self)
        top.title("Nuevo Cliente")
        top.geometry("380x320")
        top.resizable(False, False)

        ttk.Label(top, text="Nuevo Cliente", font=("Segoe UI", 12, "bold")).pack(pady=10)

        frame_form = ttk.Frame(top, padding=15)
        frame_form.pack(fill="both", expand=True)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = ttk.Entry(frame_form, width=25)
        entry_nombre.grid(row=0, column=1, pady=5)

        ttk.Label(frame_form, text="Apellido:").grid(row=1, column=0, sticky="w", pady=5)
        entry_apellido = ttk.Entry(frame_form, width=25)
        entry_apellido.grid(row=1, column=1, pady=5)

        ttk.Label(frame_form, text="Teléfono:").grid(row=2, column=0, sticky="w", pady=5)
        entry_telefono = ttk.Entry(frame_form, width=25)
        entry_telefono.grid(row=2, column=1, pady=5)

        ttk.Label(frame_form, text="Email:").grid(row=3, column=0, sticky="w", pady=5)
        entry_email = ttk.Entry(frame_form, width=25)
        entry_email.grid(row=3, column=1, pady=5)

        def guardar():
            # Ejemplo de validación de teléfono duplicado
            tel = entry_telefono.get().strip()
            if tel == "351-555-0110":
                messagebox.showerror("Error", "Ya existe un cliente registrado con ese teléfono.", parent=top)
                return
            
            if entry_nombre.get() and entry_apellido.get():
                nombre_completo = f"{entry_nombre.get()} {entry_apellido.get()}"
                self.tabla.insert("", "end", values=(nombre_completo, tel, entry_email.get(), "0"))
                top.destroy()

        frame_botones = ttk.Frame(top)
        frame_botones.pack(pady=10)
        ttk.Button(frame_botones, text="Cancelar", command=top.destroy).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Guardar", command=guardar).pack(side="left", padx=5)


class PaginaMascotas(PaginaBase):
    titulo = "Listado de Mascotas"
    subtitulo = "Administración y búsqueda general de mascotas registradas."
    def construir_contenido(self):
        frame_top = ttk.Frame(self, style="Contenido.TFrame")
        frame_top.pack(fill="x", padx=24, pady=(0, 10))

        ttk.Entry(frame_top, width=35).pack(side="left", padx=(0, 10))
        ttk.Button(frame_top, text="Buscar").pack(side="left")

        ttk.Button(frame_top, text="Eliminar").pack(side="right", padx=2)
        ttk.Button(frame_top, text="Editar").pack(side="right", padx=2)
        ttk.Button(frame_top, text="Nuevo", command=self.abrir_formulario_mascota).pack(side="right", padx=2)

        columnas = ("mascota", "raza", "dueno", "edad", "tamano", "obs")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)

        self.tabla.heading("mascota", text="Mascota")
        self.tabla.heading("raza", text="Raza")
        self.tabla.heading("dueno", text="Dueño/a")
        self.tabla.heading("edad", text="Edad")
        self.tabla.heading("tamano", text="Tamaño")
        self.tabla.heading("obs", text="Observaciones")

        datos_ejemplo = [
            ("Luna", "Caniche", "Carlos Gómez", "3", "Pequeño", "Ninguna"),
            ("Bruno", "Labrador", "Ana Ferreyra", "5", "Grande", "Piel sensible"),
            ("Toby", "Cocker", "Marcos Díaz", "2", "Mediano", "Enojo fácil"),
            ("Coco", "Golden", "Lucía Vera", "1", "Grande", "Secador lento"),
        ]

        for fila in datos_ejemplo:
            self.tabla.insert("", "end", values=fila)

        self.tabla.pack(fill="both", expand=True, padx=24, pady=(0, 20))

    def abrir_formulario_mascota(self):
        """Ventana modal con el formulario de Nueva Mascota"""
        top = tk.Toplevel(self)
        top.title("Nueva Mascota")
        top.geometry("400x380")
        top.resizable(False, False)

        ttk.Label(top, text="Nueva Mascota", font=("Segoe UI", 12, "bold")).pack(pady=10)

        frame_form = ttk.Frame(top, padding=15)
        frame_form.pack(fill="both", expand=True)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = ttk.Entry(frame_form, width=25)
        entry_nombre.grid(row=0, column=1, pady=5)

        ttk.Label(frame_form, text="Dueño/a:").grid(row=1, column=0, sticky="w", pady=5)
        combo_dueno = ttk.Combobox(frame_form, values=["Carlos Gómez", "Ana Ferreyra", "Marcos Díaz", "Lucía Vera"], width=23)
        combo_dueno.grid(row=1, column=1, pady=5)

        ttk.Label(frame_form, text="Raza:").grid(row=2, column=0, sticky="w", pady=5)
        entry_raza = ttk.Entry(frame_form, width=25)
        entry_raza.grid(row=2, column=1, pady=5)

        ttk.Label(frame_form, text="Edad:").grid(row=3, column=0, sticky="w", pady=5)
        entry_edad = ttk.Entry(frame_form, width=25)
        entry_edad.grid(row=3, column=1, pady=5)

        ttk.Label(frame_form, text="Tamaño:").grid(row=4, column=0, sticky="w", pady=5)
        combo_tamano = ttk.Combobox(frame_form, values=["Pequeño", "Mediano", "Grande"], width=23)
        combo_tamano.grid(row=4, column=1, pady=5)

        ttk.Label(frame_form, text="Observaciones:").grid(row=5, column=0, sticky="nw", pady=5)
        txt_obs = tk.Text(frame_form, width=25, height=3)
        txt_obs.grid(row=5, column=1, pady=5)

        def guardar():
            if entry_nombre.get():
                self.tabla.insert("", "end", values=(
                    entry_nombre.get(),
                    entry_raza.get(),
                    combo_dueno.get(),
                    entry_edad.get(),
                    combo_tamano.get(),
                    txt_obs.get("1.0", "end-1c")
                ))
                top.destroy()

        frame_botones = ttk.Frame(top)
        frame_botones.pack(pady=10)
        ttk.Button(frame_botones, text="Cancelar", command=top.destroy).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Guardar", command=guardar).pack(side="left", padx=5)


class PaginaTurnos(PaginaBase):
    titulo = "Listado de Turnos"
    subtitulo = "Administración y búsqueda general de citas programadas en el sistema."


class PaginaServicios(PaginaBase):
    titulo = "Servicios"
    subtitulo = "Servicios ofrecidos por la peluquería."
